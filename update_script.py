import re

with open('/home/ubuntu/debate_oil/debate_history.md', 'r') as f:
    content = f.read()

# Update the top instructions to be round-based and set language to Chinese
top_instructions = """# 多智能体辩论历史：油价与投资机会 (Multi-Agent Debate History)

本文档是多智能体关于油价及相关投资机会辩论的丰富上下文和历史记录。
**请所有智能体使用中文进行更新和辩论。**
辩论按轮次（Rounds）展开，每个智能体在自己的发言中直接提出具体的投资建议。

---

## 📋 辩论概览 (Debate Overview)

**主题:** 全球油价的未来走势与战略投资机会
**目标:** 综合各智能体（看涨、看跌、中立）的观点，形成可执行的投资洞察。
**参与者:** [智能体角色列表，例如：宏观经济智能体、地缘政治分析智能体、能源行业专家智能体]

---

## 📊 当前市场背景与基准 (Current Market Context & Baseline)

*(智能体在开始新一轮辩论前，应在此部分更新最新的宏观数据、价格水平和关键指标。)*

"""

# Find where the debate log starts
debate_log_start = content.find("## 🗣️ Debate Log")

# Find where the investment opportunities section starts and ends
inv_opp_start = content.find("## 💡 Investment Opportunities & Actionable Insights")
guidelines_start = content.find("## 📝 Guidelines for Agents Updating This File")

if debate_log_start != -1 and inv_opp_start != -1 and guidelines_start != -1:
    # Keep the debate log part, but we need to ensure the existing debate is preserved
    existing_debate = content[debate_log_start:inv_opp_start]
    
    # Update guidelines to reflect the new rules (inline investment suggestions, Chinese language)
    new_guidelines = """## 📝 智能体更新指南 (Guidelines for Agents Updating This File)

1. **按轮次追加 (Append by Rounds):** 辩论按轮次进行。请在当前轮次下追加你的观点。不要删除之前的辩论内容（除非为了修正事实错误）。
2. **使用中文 (Use Chinese):** 所有辩论内容、分析和建议必须使用中文。
3. **内联投资建议 (Inline Investment Suggestions):** **不要**在文档末尾集中列出投资机会。每个智能体必须在自己的发言段落中，直接给出具体的投资建议、逻辑和目标资产。
4. **丰富排版 (Use Rich Formatting):** 使用加粗、引用和表格来使论点清晰易读。
5. **包含可视化 (Include Visuals):** 当引用图表或数据可视化时，将图片保存到仓库的 `images/` 目录，并使用标准 Markdown 语法链接 (`![Alt text](images/filename.png)`)。
6. **注明出处 (Cite Sources):** 如果引用外部数据，请包含简短的引用或链接。

---
*最后更新由: [智能体名称] 于 [时间戳]*
"""
    
    # Construct the final content
    final_content = top_instructions + existing_debate + new_guidelines
    
    with open('/home/ubuntu/debate_oil/debate_history.md', 'w') as f:
        f.write(final_content)
    print("File updated successfully.")
else:
    print("Could not find the expected sections in the markdown file.")
