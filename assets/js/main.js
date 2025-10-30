// assets/js/main.js
// SPELLs Group Main Interaction Script
// Designed for smooth, minimal, and scientific-style transitions

document.addEventListener("DOMContentLoaded", () => {
  console.log("SPELLs website loaded.");

  // === 1. Glass Navbar Scroll Effect ===
  const navbar = document.querySelector(".navbar");
  window.addEventListener("scroll", () => {
    if (window.scrollY > 50) {
      navbar.classList.add("scrolled");
    } else {
      navbar.classList.remove("scrolled");
    }
  });

  // === 2. Fade-in Animation on Scroll ===
  const fadeElems = document.querySelectorAll(".fade-in");
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
      }
    });
  }, { threshold: 0.15 });

  fadeElems.forEach(el => observer.observe(el));

  // === 3. Card Hover Glow Effect ===
  const cards = document.querySelectorAll(".card, .member-card");
  cards.forEach(card => {
    card.addEventListener("mousemove", e => {
      const rect = card.getBou
