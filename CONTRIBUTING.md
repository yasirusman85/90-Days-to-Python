# Contributing Guidelines & Student Submission Guide 🤝

Welcome! This guide explains how you, as a student or a collaborator, can use this repository to track your progress, build your personal coding portfolio, and suggest enhancements to the core curriculum.

---

## 🎒 How Students Should Use This Repo

This repository is designed to be your **interactive workbook**. To use it as your personal learning diary and showcase your work to prospective employers:

### 1. Fork and Clone
Fork the repository to your own GitHub account, and clone it locally. 

### 2. Daily Learning Workflow
For each day of the challenge:
1. **Study**: Go to the active week's folder (e.g., `weeks/week_01_basics_and_setup/`) and read the lesson inside its `README.md`.
2. **Code**: Navigate to that week's `daily_tasks/` folder. Open the template script for that day (e.g., `day_02_variables.py`), write your code, and solve the exercises.
3. **Log**: Copy the markdown from [templates/daily_log_template.md](file:///./templates/daily_log_template.md), create a new file or add a section in your personal progress journal, and fill in what you learned, what code you wrote, any blockers you had, and how you solved them.
4. **Commit**: Save your progress and push it to your fork!
   ```bash
   git add .
   git commit -m "Day 2 completed: Variables and simple operators"
   git push origin main
   ```
5. **Mark Done**: Update the checkboxes `[ ]` in the main `README.md` to `[x]` as you complete days.

---

## 🛠️ How Collaborators Can Contribute

If you are an educator, mentor, or developer looking to enhance this curriculum:

1. **Submit Bug Reports or Feature Requests**: Use GitHub Issues to report typos, incorrect code examples, or suggest new tool features.
2. **Submit Pull Requests (PRs)**:
   - Create a feature branch off `main` (e.g., `git checkout -b fix/typo-day-15`).
   - Keep your changes focused. If fixing code, ensure PEP 8 styles are followed.
   - Submit your PR, and describe your modifications clearly in the description.

---

## 🐍 Style Guide & Coding Standards

To maintain clean and readable code throughout the repository, please adhere to:
*   **PEP 8 Formatting**: Keep line lengths below 79 characters, use 4 spaces for indentation, and write descriptive variable names in `snake_case`.
*   **Comments**: Explain *why* a particular piece of code works, rather than just *what* it does.
*   **Docstrings**: Use triple-quotes `"""` at the beginning of custom functions to describe what the function does, its parameters, and its return values.

Happy Coding! 💻
