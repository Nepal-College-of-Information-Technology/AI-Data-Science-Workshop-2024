# AI & Data Science Workshop 2024: Project Work


**Project Submission Deadline: 15th of November 2024**

---

## Instructions

### 1. Join the Discord Channel
- **1.**: Join the **AI & Data Science Workshop 2024** Discord server.
- **2.**: Navigate to the **#project-teams** channel, which is under the **INFORMATION** category.
- **3.**: Select your project group by clicking to the relevant group number. Once you've selected your group, you'll automatically join the corresponding team channel (e.g., **#team-1**, **#team-2**, etc.).
- **4.**: Introduce yourself in your team’s channel and start collaborating with your team members.

### 2. Join the GitHub Classroom Group Assignment
- **1.**: Once you have joined your project group, your next i. s to join the **GitHub Classroom group assignment** via the invite link shared on Discord.
- **2.**: Your team will have its own repository where you will collaboratively work on the project.
- **3.**: You can create as many branches as needed to work on different parts of the project. Use branch names like `feature-yourname` to organize work and contributions.
- **4.**: Submit the final project by merging all the branches and submitting a pull request before the deadline.

---
### GitHub-Discord Integration (Webhooks)
To keep track of updates on GitHub within the Discord channel, you need to add a webhook to your GitHub repository. Follow these steps:

1. : Navigate to your repository's Settings.
2. : Click on Webhooks in the left sidebar.
3. : Click the Add Webhook button.
4. : In the Payload URL, enter your Discord webhook URL (this can be obtained from the me{Ask me to Create a Webhook for your channel}).
5. : Choose application/json as the content type.
6. : Set Which events would you like to trigger this webhook? to Send me everything.
7. : Click Add Webhook to save.
Once set up, any push or pull request made to the GitHub repository will automatically be sent to your group's Discord channel.

---
### Group Discussion:
#### Today’s Task: Discuss with your team members and prepare a draft project abstract.
The abstract should summarize:

**Problem Statement:** What problem is your project trying to solve?

**AI Techniques:** Which AI/ML techniques will you use?

**Datasets:** What dataset(s) will you use for training and testing?

**Project Plan:** Briefly outline the steps your team will take to complete the project.

**Deadline:** Submit your project abstract by tomorrow (Day 15) to the instructor via Discord.

---
## Project Structure

Here is a suggested structure for your project:

```plaintext
project-directory/
├── data/                   # Data files for the project
│   ├── raw/                # Raw data files
│   └── processed/          # Processed datasets for modeling
│
├── notebooks/              # Jupyter Notebooks for experimentation
│   ├── exploration.ipynb   # Data exploration notebook
│   └── model_training.ipynb # Model training and evaluation
│
├── src/                    # Source code
│   ├── data_preprocessing.py # Data preprocessing script
│   ├── train_model.py      # Model training script
│   └── evaluate_model.py   # Model evaluation script
│
├── reports/                # Reports and presentations
│   └── final_report.pdf    # Final project report
│   └── presentation.pptx   # Final presentation slides
│
├── README.md               # This README file
└── requirements.txt        # Dependencies for the project
