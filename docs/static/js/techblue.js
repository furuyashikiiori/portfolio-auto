document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".tb-link").forEach((btn) => {
    
    const overlay = document.createElement("span");
    overlay.className = "tb-link-overlay";
    btn.appendChild(overlay);

    btn.addEventListener("mouseenter", () => {
      overlay.style.transform = "scaleX(1)";
    });

    btn.addEventListener("mouseleave", () => {
      overlay.style.transform = "scaleX(0)";
    });
  });
});
