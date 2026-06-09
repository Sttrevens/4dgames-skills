# 4D Games Skills

[English](README.en.md)

4D Games Skills 是 4D Games 从游戏开发、Agent 自动化和个人系统里沉淀出来的一组可复用 agent skills。

它不是 prompt 合集。每个 skill 都是一个给 agent 使用的紧凑工作规程：什么时候触发、该看什么上下文、如何行动、完成前需要哪些验证或交接证据。

这个仓库采用 **索引优先** 的结构：每个 skill 都有自己的独立仓库作为 source of truth；本仓的 `skills/` 目录只是安装/浏览镜像。

## 安装

目前可以把 agent 或 skills CLI 指向本仓库里的具体目录：

```bash
# 示例路径
skills/air-game-dev-pm
```

## Skills

<!-- SKILLS:START -->
| Skill | 分类 | 描述 |
|---|---|---|
| [`agentic-automation-review-gate`](https://github.com/Sttrevens/agentic-automation-review-gate-skill) | Agent 运维 | 在合并、部署或对外声称可靠之前，审查 recurring agent automation 的产出和证据。 |
| [`4d-bot-integration`](https://github.com/Sttrevens/4d-bot-integration-skill) | Bot 运行时 | 安全处理 4D Games bot runtime、飞书/Lark channel worker、租户边界和 Codex worker 交接。 |
| [`learning-project-planner`](https://github.com/Sttrevens/learning-project-planner-skill) | 个人系统 | 把一个学习主题变成可持续项目：路线图、长期上下文、仪表盘和第一周课程。 |
| [`personal-health-pulse`](https://github.com/Sttrevens/personal-health-pulse-skill) | 个人系统 | 构建或运行本地优先的个人健康记录与教练 agent，支持任意消息通道。 |
| [`air-game-dev-pm`](https://github.com/Sttrevens/air-game-dev-pm-skill) | 游戏制作 | 从玩家体验出发，把游戏规划拆成支柱、特性、验证等级、任务和可验收迭代石头。 |
| [`steam-launch-forecast`](https://github.com/Sttrevens/steam-launch-forecast-skill) | 游戏商业 | 基于愿望单、Steam/社区信号、区域需求和可比游戏，预测 Steam 首发表现。 |
<!-- SKILLS:END -->

## 设计原则

- `SKILL.md` 要足够精简，适合进入 agent 的上下文窗口。
- 长 schema、例子和实现细节放进 `references/`。
- 不公开私人路径、用户 ID、租户 ID、聊天记录、客户数据、API token 或内部部署密钥。
- 优先沉淀能产生证据的工作流：测试、截图、报告、分支名、验收标准、回滚信号和 next-stone handoff。
- 把 local-first trust 当成产品能力，而不是附带要求。

## 开发

编辑 `skills.yaml` 和对应的 `skills/<name>/SKILL.md`，然后运行：

```bash
python3 scripts/render_readme.py
python3 scripts/validate_skills.py
```

README 和 README.en.md 的 skill 表格都由 `skills.yaml` 渲染。独立仓库 skill 的镜像可通过 `python3 scripts/sync_skills.py` 更新。
