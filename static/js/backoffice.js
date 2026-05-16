const body = document.body;
const sidebar = document.getElementById('sidebar');
const toggleButton = document.getElementById('sidebarToggle');
const sidebarOverlay = document.getElementById('sidebarOverlay');
const sidebarClose = document.getElementById('sidebarClose');

let isMenuOpen = false;

window.addEventListener('DOMContentLoaded', () => {
  const currentUrl = window.location.href;
  const isBackofficePage = currentUrl.includes('/backoffice');

  body.classList.add('backoffice-page');
  if (isBackofficePage) {
    openSidebar();
  } else {
    closeSidebar();
  }
});

const openSidebar = () => {
  sidebar.classList.add('open');
  sidebar.classList.remove('closed');
  toggleButton.classList.add('hidden');
  body.classList.add('sidebar-open');
  toggleButton.setAttribute('aria-label', 'Fechar menu');
  isMenuOpen = true;
};

const closeSidebar = () => {
  sidebar.classList.add('closed');
  sidebar.classList.remove('open');
  toggleButton.classList.remove('hidden');
  body.classList.remove('sidebar-open');
  toggleButton.setAttribute('aria-label', 'Abrir menu');
  isMenuOpen = false;
};

const toggleSidebar = () => {
  if (isMenuOpen) {
    closeSidebar();
  } else {
    openSidebar();
  }
};

toggleButton?.addEventListener('click', toggleSidebar);
sidebarClose?.addEventListener('click', closeSidebar);
sidebarOverlay?.addEventListener('click', closeSidebar);
