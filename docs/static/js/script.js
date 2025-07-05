// 最初のスキル行を 1 行生成
window.addEventListener("DOMContentLoaded", () => {
  addSkillRow();
  addProjectRow();
});

const skillTmpl = document.getElementById("skill-row-template");
const skillContainer = document.getElementById("skills-container");
const addSkillBtn = document.getElementById("add-skill-btn");

const projectTmpl = document.getElementById("project-row-template");
const projectContainer = document.getElementById("projects-container");
const addProjectBtn = document.getElementById("add-project-btn");

addSkillBtn.addEventListener("click", () => addSkillRow());
addProjectBtn.addEventListener("click", () => addProjectRow());

function addSkillRow() {
  const clone = skillTmpl.content.firstElementChild.cloneNode(true);

  // 削除ボタン設定
  clone.querySelector(".delete-btn").onclick = () => {
    if (skillContainer.children.length > 1) {
      clone.remove();
    }
  };

  skillContainer.appendChild(clone);
}

function addProjectRow() {
  const clone = projectTmpl.content.firstElementChild.cloneNode(true);

  // 削除ボタン設定
  clone.querySelector(".delete-btn").onclick = () => {
    if (projectContainer.children.length > 1) {
      clone.remove();
    }
  };

  projectContainer.appendChild(clone);
}
