// 最初のスキル行を 1 行生成
window.addEventListener("DOMContentLoaded", () => addSkillRow());

const tmpl = document.getElementById("skill-row-template");
const container = document.getElementById("skills-container");
const addBtn = document.getElementById("add-skill-btn");

addBtn.addEventListener("click", () => addSkillRow());

function addSkillRow() {
  const clone = tmpl.content.firstElementChild.cloneNode(true);

  // 削除ボタン設定
  clone.querySelector(".delete-btn").onclick = () => {
    if (container.children.length > 1) {
      clone.remove();
    }
  };

  container.appendChild(clone);
}
