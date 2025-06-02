# VLA Tasks
This repository aim to collect a set of tasks for the VLA (Vision-Language Agent) to learn from. The tasks are designed to be diverse, covering various aspects of vision and language understanding.

Please follow the instructions below to set up the environment, bid on tasks, and contribute new tasks:

## Installation Instructions
Berfore you can start working on the tasks, you need to set up the environment. The installation process may vary depending on your operating system.

We prepare a set of installation instructions to help you set up the environment for running the tasks.
- [Installation Guide for LIBERO on Windows](./docs/install_win.md)
- [Installation Guide for LIBERO on Linux](./docs/install_linux.md)
- [Installation Guide for LIBERO on MacOS](./docs/install_macos.md)

> **Note:** We tried to install LIBERO on WSL and virtual machines, but neither of them worked well. 

## Bid your tasks
We have provided a list of tasks (task instructions) [here](https://docs.google.com/spreadsheets/d/1ElB9GhiSfXJpvrUI0Efa5lJglc_rO-LLGUUT_vosmoQ/edit?usp=sharing). You are going to bid on tasks you want to define first and begin your annotation. 

To "bid" your task, you need to:
1. **Check the task list**: Look at the [task list](https://docs.google.com/spreadsheets/d/1ElB9GhiSfXJpvrUI0Efa5lJglc_rO-LLGUUT_vosmoQ/edit?usp=sharing) to see if the task you want to define is already taken.
2. **Add your name**: If the task is not taken, add your name to the "Designer" column of the task list.

Once you have added your name, you can start working on the task definition and reward code.

## Task definition and Contribution
#### Overview
To contribute a new task, you need to
- create a pull request with your task definition and reward code 
- and add your task with video demonstration in this [google sheet](https://docs.google.com/spreadsheets/d/1ElB9GhiSfXJpvrUI0Efa5lJglc_rO-LLGUUT_vosmoQ/edit?usp=sharing). 

> Your task will be reviewed by the team and added to the repository if it meets the requirements.

#### Annotation
Please follow the [annotation guideline](./docs/annotation_guideline.md) to implement your task in the `tasks` directory. 

The guideline provides detailed instructions on how to define a task and how to write the reward code for the task. Also, it provide examples of existing tasks to help you understand the structure and requirements.

#### Submission
Please follow the [submission guideline](./docs/submission_guideline.md) to submit your task. 

The guideline provides step-by-step instructions on how to fork the repository, create a new branch, add your task, and create a pull request.