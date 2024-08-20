#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
import random
import time

# 定义职业和专精的列表（已翻译成中文）
classes_and_specs = {
    "战士": ["武器", "狂怒", "防护"],
    "圣骑士": ["神圣", "防护", "惩戒"],
    "猎人": ["野兽控制", "射击", "生存"],
    "潜行者": ["刺杀", "狂徒", "敏锐"],
    "牧师": ["戒律", "神圣", "暗影"],
    "死亡骑士": ["鲜血", "冰霜", "邪恶"],
    "萨满祭司": ["元素", "增强", "恢复"],
    "法师": ["奥术", "火焰", "冰霜"],
    "术士": ["痛苦", "恶魔学识", "毁灭"],
    "武僧": ["酒仙", "织雾", "踏风"],
    "德鲁伊": ["平衡", "野性", "守护", "恢复"],
    "恶魔猎手": ["浩劫", "复仇"],
    "唤魔师": ["毁灭", "恢复"],
}

# 标题
st.title("魔兽世界职业与专精随机选择器")

# 按钮状态控制
start_button = st.button("开始")
stop_button = st.button("停止")

# 初始化session state
if "running" not in st.session_state:
    st.session_state.running = False
if "selected_class" not in st.session_state:
    st.session_state.selected_class = None
if "selected_spec" not in st.session_state:
    st.session_state.selected_spec = None

# 创建一个空的容器来显示职业和专精
placeholder = st.empty()

# 开始按钮逻辑
if start_button and not st.session_state.running:
    st.session_state.running = True
    while st.session_state.running:
        st.session_state.selected_class = random.choice(list(classes_and_specs.keys()))
        st.session_state.selected_spec = random.choice(classes_and_specs[st.session_state.selected_class])

        # 在容器中更新所有职业和专精列表，突出显示当前选择
        with placeholder.container():
            st.write("职业与专精列表：")
            for class_name, specs in classes_and_specs.items():
                if class_name == st.session_state.selected_class:
                    st.markdown(f"**> {class_name}**")
                    for spec in specs:
                        if spec == st.session_state.selected_spec:
                            st.markdown(f"**   - {spec}**")
                        else:
                            st.write(f"   - {spec}")
                else:
                    st.write(f"{class_name}")
                    for spec in specs:
                        st.write(f"   - {spec}")

        time.sleep(0.1)  # 控制滚动速度

# 停止按钮逻辑
if stop_button:
    st.session_state.running = False
    with placeholder.container():
        st.write(f"**最终选择**")
        st.write(f"**职业: {st.session_state.selected_class}**")
        st.write(f"**专精: {st.session_state.selected_spec}**")


# In[ ]:




