const body = document.body;
const sidebar = document.getElementById('sidebar');
const toggleButton = document.getElementById('sidebarToggle');
const sidebarOverlay = document.getElementById('sidebarOverlay');
const sidebarClose = document.getElementById('sidebarClose');

const openSidebar = () => {
  sidebar.classList.add('open');
  sidebar.classList.remove('closed');
  toggleButton.classList.add('hidden');
  body.classList.add('sidebar-open');
  toggleButton.setAttribute('aria-label', 'Fechar menu');
};

const closeSidebar = () => {
  sidebar.classList.add('closed');
  sidebar.classList.remove('open');
  toggleButton.classList.remove('hidden');
  body.classList.remove('sidebar-open');
  toggleButton.setAttribute('aria-label', 'Abrir menu');
};

const toggleSidebar = () => {
  if (sidebar.classList.contains('open')) {
    closeSidebar();
  } else {
    openSidebar();
  }
};

window.addEventListener('DOMContentLoaded', () => {
  body.classList.add('backoffice-page');
  if (window.innerWidth <= 900) {
    closeSidebar();
  } else {
    openSidebar();
  }
});

toggleButton?.addEventListener('click', toggleSidebar);
sidebarClose?.addEventListener('click', closeSidebar);
sidebarOverlay?.addEventListener('click', closeSidebar);

window.addEventListener('resize', () => {
  if (window.innerWidth <= 900) {
    closeSidebar();
  } else {
    openSidebar();
  }
});
