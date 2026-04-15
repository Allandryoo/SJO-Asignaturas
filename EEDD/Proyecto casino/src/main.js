// ===== Chips & Chips — Floating Gold Particles =====
// Matches the "Obsidian Atrium" design system
(function createParticles() {
  const container = document.getElementById('particles');
  if (!container) return;

  const count = 45;
  const colors = [
    'rgba(242, 202, 80, 0.5)',   // primary
    'rgba(212, 175, 55, 0.4)',   // primary-container
    'rgba(255, 224, 136, 0.3)',  // primary-fixed
    'rgba(233, 195, 73, 0.35)', // primary-dim
    'rgba(245, 198, 141, 0.2)', // tertiary
    'rgba(215, 171, 116, 0.25)', // tertiary-container
  ];

  for (let i = 0; i < count; i++) {
    const p = document.createElement('div');
    p.classList.add('particle');

    const size = Math.random() * 3.5 + 0.8;
    const color = colors[Math.floor(Math.random() * colors.length)];

    p.style.width = size + 'px';
    p.style.height = size + 'px';
    p.style.left = Math.random() * 100 + '%';
    p.style.background = color;
    p.style.boxShadow = `0 0 ${size * 4}px ${color}`;
    p.style.animationDuration = (Math.random() * 15 + 10) + 's';
    p.style.animationDelay = (Math.random() * 12) + 's';

    container.appendChild(p);
  }
})();
