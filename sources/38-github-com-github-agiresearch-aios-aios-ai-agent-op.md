---
url: "https://github.com/agiresearch/AIOS"
title: "GitHub - agiresearch/AIOS: AIOS: AI Agent Operating System · GitHub"
engine: brave
rank: 38
published: unknown
updated: unknown
author: unknown
org: GitHub
char_count: 9428
fetched_at: "2026-05-31T17:39:43.343649+00:00"
---

AIOS is the AI Agent Operating System, which embeds large language model (LLM) into the operating system and facilitates the development and deployment of LLM-based AI Agents. AIOS is designed to address problems (e.g., scheduling, context switch, memory management, storage management, tool management, Agent SDK management, etc.) during the development and deployment of LLM-based agents, towards a better AIOS-Agent ecosystem for agent developers and agent users. AIOS includes the AIOS Kernel (this repository) and the AIOS SDK (the repository). AIOS supports both Web UI and Terminal UI.  
The AIOS system is comprised of two key components: the AIOS kernel and the AIOS SDK. The AIOS kernel acts as an abstraction layer over the operating system kernel, managing various resources that agents require, such as LLM, memory, storage and tool. The AIOS SDK is designed for agent users and developers, enabling them to build and run agent applications by interacting with the AIOS kernel. AIOS kernel is the current repository and AIOS SDK can be found at 
Below shows how agents utilize AIOS SDK to interact with AIOS kernel and how AIOS kernel receives agent queries and leverage the chain of syscalls that are scheduled and dispatched to run in different modules.
For computer-use agent, the architecture extends the AIOS Kernel with significant enhancements focused on computer contextualization. While preserving essential components like LLM Core(s), Context Manager, and Memory Manager, the Tool Manager module has been fundamentally redesigned to incorporate a VM (Virtual Machine) Controller and MCP Server. This redesign creates a sandboxed environment that allows agents to safely interact with computer systems while maintaining a consistent semantic mapping between agent intentions and computer operations.
  * 🎉 The foundational paper has been accepted by the Conference on Language Modeling (COLM 2025). Congratulations to the team!
  * 🎉 AIOS has been selected as the finalist for AgentX – LLM Agents MOOC Competition, hosted by Berkeley RDI in conjunction with the Advanced LLM Agents MOOC. Congratulations to the team!
  * 📋 Paper has been accepted by NAACL 2025! Features has been integrated into .
  * 🔥 A major refactor of the codebase packed with powerful new features have been integrated into the main repo. Please check out the AIOS v0.2.2 release.
  * 📋 Our paper has been accepted by ICLR2025! The features of this paper has been integrated into AIOS as the .
  * 🔥 Deepseek-r1 (1.5b, 7b, 8b, 14b, 32b, 70b, 671b) has already been supported in AIOS, both open-sourced versions and deepseek apis (deepseek-chat and deepseek-reasoner) are available.
  * 🔥 AIOS supports multiple agent creation frameworks (e.g., ReAct, Reflexion, OpenAGI, AutoGen, Open Interpreter, MetaGPT). Agents created by these frameworks can onboard AIOS. Onboarding guidelines can be found at the .
  * 🚀 More agents with ChatGPT-based tool calling are added (i.e., MathAgent, RecAgent, TravelAgent, AcademicAgent and CreationAgent), their profiles and workflows can be found in .
  * 🤝 AIOS is up. Welcome to join the community for discussions, brainstorming, development, or just random chats! For how to contribute to AIOS, please see .
  * 📋 After several months of working, our perspective paper is officially released.


  * : Central server that hosts the agent marketplace/repository where users can publish, download, and share agents. Acts as the distribution center for all agent-related resources.
  * : Client machine that provides user interface for interacting with agents. Can be any device from mobile phones to desktops that supports agent visualization and control.
  * : Development environment where agent developers write, debug and test their agents. Requires proper development tools and libraries.
  * : Execution environment where agents actually run and perform tasks. Needs adequate computational resources for agent operations.


The following parts introduce different modes of deploying AIOS. 
  * Features: 
    * For agent developers: They can develop and test agents in Machine A and can upload agents to agent hub on Machine B.


  * Features: 
    * Remote use of agents: Agent users / developers can use agents on Machine B, which is different from the development and running machine (Machine A).


  * Features: 
    * Remote development of agents: Agent developers can develop their agents on Machine B while running and testing their agents in Machine A. Benefit developers who would like to develop agents on resource-restricted machine (e.g., mobile device or edge device)


  *     * Each user/developer can have their personal AIOS with long-term persistent data as long as they have registered account in the AIOS ecosystem
  * 

  * Critical techniques: 


To use the mcp for computer-use agent, we strongly recommend you install a virtualized environment equipped with GUI. Instructions can be found in .
: The machine where the AIOS kernel (AIOS) is installed must also have the AIOS SDK (Cerebrum) installed. Installing AIOS kernel will install the AIOS SDK automatically by default. If you are using the Local Kernel mode, i.e., you are running AIOS and agents on the same machine, then simply install both AIOS and Cerebrum on that machine. If you are using Remote Kernel mode, i.e., running AIOS on Machine 1 and running agents on Machine 2 and the agents remotely interact with the kernel, then you need to install both AIOS kernel and AIOS SDK on Machine 1, and install the AIOS SDK alone on Machine 2. Please follow the guidelines at regarding how to install the SDK.
Before launching AIOS, it is required to set up configurations. AIOS provides two ways of setting up configurations, one is to set up by directly modifying the configuration file, another is to set up interactively.
You need API keys for services like OpenAI, Anthropic, Groq and HuggingFace. The simplest way to configure them is to edit the .
It is important to mention that, we strongly recommend using the file to set up your API keys. This method is straightforward and helps avoid potential sychronization issues with environment variables.
vLLM currently only supports Linux and GPU-enabled environments. If you don't have a compatible environment, please choose other backend options. To enable the tool calling feature of vllm, refer to 



You also need to set up the host and port in the configuration of Cerebrum (AIOS SDK) to make sure it is consistent with the configurations of AIOS.
Command to launch the kernel in the background so it continues running even after the active shell is closed, while also logging information to the specified log file (recommended):
To interact with the AIOS terminal (LLM-based semantic file system), you can run the following command to start the AIOS terminal.
The rollback feature of the AIOS terminal requires the connection to the redis server. Make sure you have the redis server running if you would like to use the rollback feature.
Make sure you have installed a virtualized environment with GUI, then you can refer to for how to run the computer-use agent.  
An early experimental Rust scaffold lives in providing trait definitions and minimal placeholder implementations (context, memory, storage, tool, scheduler, llm). This is NOT feature-parity yet; it's a foundation for incremental porting and performance-focused components.

```
@article{mei2025aios,
  title={AIOS: LLM Agent Operating System},
  author={Mei, Kai and Zhu, Xi and Xu, Wujiang and Hua, Wenyue and Jin, Mingyu and Li, Zelong and Xu, Shuyuan and Ye, Ruosong and Ge, Yingqiang and Zhang, Yongfeng}
  journal={In Proceedings of the 2nd Conference on Language Modeling (COLM 2025)},
  year={2025}
}
@article{mei2025litecua,
  title={LiteCUA: Computer as MCP Server for Computer-Use Agent on AIOS},
  author={Mei, Kai and Zhu, Xi and Gao, Hang and Lin, Shuhang and Zhang, Yongfeng},
  journal={arXiv preprint arXiv:2505.18829},
  year={2025}
}
@article{xu2025mem,
  title={A-Mem: Agentic Memory for LLM Agents},
  author={Xu, Wujiang and Liang, Zujie and Mei, Kai and Gao, Hang and Tan, Juntao and Zhang, Yongfeng},
  journal={arXiv:2502.12110},
  year={2025}
}
@inproceedings{rama2025cerebrum,
  title={Cerebrum (AIOS SDK): A Platform for Agent Development, Deployment, Distribution, and Discovery}, 
  author={Balaji Rama and Kai Mei and Yongfeng Zhang},
  booktitle={2025 Annual Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics},
  year={2025}
}
@inproceedings{shi2025from,
  title={From Commands to Prompts: {LLM}-based Semantic File System for AIOS},
  author={Zeru Shi and Kai Mei and Mingyu Jin and Yongye Su and Chaoji Zuo and Wenyue Hua and Wujiang Xu and Yujie Ren and Zirui Liu and Mengnan Du and Dong Deng and Yongfeng Zhang},
  booktitle={The Thirteenth International Conference on Learning Representations},
  year={2025},
  url={https://openreview.net/forum?id=2G021ZqUEZ}
}
@article{ge2023llm,
  title={LLM as OS, Agents as Apps: Envisioning AIOS, Agents and the AIOS-Agent Ecosystem},
  author={Ge, Yingqiang and Ren, Yujie and Hua, Wenyue and Xu, Shuyuan and Tan, Juntao and Zhang, Yongfeng},
  journal={arXiv:2312.03815},
  year={2023}
}

```

If you would like to join the community, ask questions, chat with fellows, learn about or propose new features, and participate in future developments, join our !

