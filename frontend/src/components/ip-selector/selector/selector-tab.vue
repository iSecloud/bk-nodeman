<template>
  <div class="selector-tab">
    <div class="selector-tab-header"
         ref="tabwrapper"
         v-show="tabVisible && panels.length"
         v-resize="handleResize">
      <ul class="selector-tab-horizontal" ref="tabcontent">
        <li v-for="item in panels"
            :key="item.name"
            :class="[
              'tab-item',
              { 'active': active === item.name },
              { 'disabled': item.disabled }
            ]"
            v-show="!item.hidden && !hiddenPanels.some(data => data.name === item.name)"
            :data-name="item.name"
            v-bk-tooltips.top="{
              disabled: !item.disabled || !item.tips,
              content: item.tips,
              delay: [300, 0]
            }"
            ref="tabItem"
            @click="!item.disabled && handleTabChange(item)">
          <slot name="label" v-bind="{ item }">
            {{ item.label }}
          </slot>
        </li>
        <li v-show="showArrow" @click="handleShowList">
          <span class="selector-tab-all">
            <i class="bk-icon icon-angle-double-right"></i>
          </span>
        </li>
      </ul>
    </div>
    <div class="selector-tab-content" :style="{ 'border-top': tabVisible && panels.length ? `none` : '' }">
      <slot></slot>
    </div>
  </div>
</template>
<script lang="ts">
import { Component, Vue, Prop, Model, Emit, Ref } from 'vue-property-decorator';
import { IPanel } from '../types/selector-type';
import { Debounce, hasOwnProperty } from '../common/util';
import { resize } from '../common/observer-directive';
import Menu from '../components/menu.vue';

@Component({
  name: 'selector-tab',
  directives: {
    resize,
  },
})
export default class SelectorTab extends Vue {
  @Model('tab-change', { default: '', type: String }) private readonly active!: string;
  @Prop({
    default: () => [],
    type: Array,
    validator: (v: IPanel[]) => {
      const item = v.find((item: IPanel) => !hasOwnProperty(item, ['name', 'label']));
      item && console.warn(item, '缺少必要属性');
      return !item;
    },
  })
  private readonly panels!: IPanel[];
  @Prop({ default: true, type: Boolean }) private readonly tabVisible!: boolean;

  @Ref('tabwrapper') private readonly tabwrapper!: HTMLElement;
  @Ref('tabcontent') private readonly tabcontent!: HTMLElement;
  @Ref('tabItem') private readonly tabItemRef!: HTMLElement[];

  private hiddenPanels: { name: string, width: number }[] = [];
  private popoverInstance: any = null;
  private menuInstance: Menu | null = null;

  private get showArrow() {
    return this.hiddenPanels.length !== 0;
  }

  private beforeDestroy() {
    if (this.menuInstance) {
      this.menuInstance.$off('click', this.handleMenuClick);
      this.menuInstance.$destroy();
    }
  }

  private handleMenuClick(menu: IPanel) {
    this.handleTabChange(menu);
    this.popoverInstance && this.popoverInstance.hide();
  }

  private handleShowList(event: Event) {
    if (!event.target) return;

    if (!this.menuInstance) {
      this.menuInstance = new Menu().$mount();
      this.menuInstance.$props.list = this.panels;

      this.menuInstance.$off('click', this.handleMenuClick);
      this.menuInstance.$on('click', this.handleMenuClick);
    }

    if (!this.popoverInstance) {
      this.popoverInstance = this.$bkPopover(event.target, {
        content: this.menuInstance.$el,
        trigger: 'manual',
        arrow: false,
        theme: 'light ip-selector',
        maxWidth: 280,
        offset: '0, 0',
        sticky: true,
        duration: [275, 0],
        interactive: true,
        boundary: 'window',
        placement: 'bottom',
      });
    }
    this.popoverInstance.show();
  }

  @Emit('tab-change')
  private handleTabChange(panel: IPanel) {
    return panel.name;
  }

  @Debounce(400)
  private handleResize() {
    if (!this.tabwrapper || !this.tabcontent) return;

    const { right: wrapperRight } = this.tabwrapper.getBoundingClientRect();

    this.tabItemRef && this.tabItemRef.forEach((node) => {
      const { right: nodeRight, width: nodeWidth } = (node as HTMLElement).getBoundingClientRect();
      const nameData = (node as HTMLElement).dataset.name;
      const index = this.hiddenPanels.findIndex(item => item.name === nameData);
      // 32: 折叠按钮宽度
      if ((nodeRight + 32) > wrapperRight) {
        (index === -1) && nameData && this.hiddenPanels.push({
          name: nameData,
          width: nodeWidth,
        });
      }
    });

    this.$nextTick(() => {
      const wrapperWidth = this.tabwrapper.clientWidth;
      let contentWidth = this.tabcontent.clientWidth;
      // 按顺序显示panel
      this.panels.forEach((item) => {
        const index = this.hiddenPanels.findIndex(data => data.name === item.name);
        if (index > -1 && (contentWidth + this.hiddenPanels[index].width) < wrapperWidth) {
          contentWidth += this.hiddenPanels[index].width;
          this.hiddenPanels.splice(index, 1);
        }
      });
    });
  }
}
</script>
<style lang="scss" scoped>
.selector-tab {
  display: flex;
  flex-direction: column;
  &-header {
    display: flex;
    align-items: center;
    border: 1px solid #dcdee5;
    border-radius: 2px;
    background: #fafbfd;
  }
  &-content {
    flex: 1;
    height: 0;
    border: 1px solid #dcdee5;
  }
}
.selector-tab-horizontal {
  display: flex;
  flex-shrink: 0;
  margin-bottom: -1px;
}
.tab-item {
  height: 42px;
  display: flex;
  align-items: center;
  font-size: 14px;
  color: #63656e;
  padding: 0 24px;
  border-right: 1px solid #dcdee5;
  border-bottom: 1px solid #dcdee5;
  cursor: pointer;
  outline: 0;
  &.disabled {
    color: #c4c6cc;
    cursor: not-allowed;
  }
  &.visibility {
    visibility: hidden;
  }
}
.tab-item.active {
  color: #313238;
  background: #fff;
  border-bottom: 0;
}
.selector-tab-all {
  font-size: 20px;
  width: 32px;
  height: 42px;
  line-height: 42px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  cursor: pointer;
  i {
    outline: 0;
  }
}
</style>
