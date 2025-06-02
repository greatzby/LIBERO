# Submission Guideline
## Things to do
1. **Fork the repository**: Create a personal copy of the repository on your GitHub account.
2. **Clone the repository**: Download your forked repository to your local machine using `git clone <your-fork-url>`.
3. **Create a new branch**: Before making changes, create a new branch for your task using `git checkout -b <branch-name>`.
4. **Add your task**: Follow the [annotation guideline](./docs/annotation_guideline.md) to implement your task in the `tasks` directory.
5. **Check your task**: Record the video of you successfully finishing the task via teleoperation.
6. **Update the task list**: Add your task to the [task list](https://docs.google.com/spreadsheets/d/1ElB9GhiSfXJpvrUI0Efa5lJglc_rO-LLGUUT_vosmoQ/edit?gid=0#gid=0) with a link to the video demonstration.
7. **Push your changes**: After completing your task, add and commit your changes to your branch using `git add .` and `git commit -m "Add task <task-name>"`. Then push your changes to your forked repository using `git push origin <branch-name>`.
8. **Create a pull request**: Go to the original repository and create a pull request from your branch. Provide a clear description of your task and any relevant information.
9. **Add the Link to pr on the task list**: After creating the pull request, add the link to your pull request in the [task list](https://docs.google.com/spreadsheets/d/1ElB9GhiSfXJpvrUI0Efa5lJglc_rO-LLGUUT_vosmoQ/edit?gid=0#gid=0) under the "PR" column.
10. **Wait for review**: The team will review your pull request. If any changes are needed, they will provide feedback. Make the necessary changes and push them to your branch.

## Important Notes
You should **only**:
- add a new file for each task in the tasks folder,
- add a new predicate in `base_predicate.py`, and also `_init_.py`

**Don't**:
- modify the existing files in the tasks folder,
- modify the existing predicates in `base_predicate.py` or `_init_.py`.
- modify the existing tasks.

## What to include in the google sheet
- **Task Scene**: The scene you used for the task.
- **Task instructions**: A clear and concise description of the task, including the goal and any specific requirements.
- **Teleoperation test video link**: A link to the video demonstrating the successful completion of your task via teleoperation.
- **Reward implementation**: your goal state
- **Potential reward hack**: list potential reward hacking cases and how your reward implementation can eliminate this
- **PR link**: link to your PR
- **Designer**: your name
