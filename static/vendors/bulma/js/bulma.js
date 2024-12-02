document.addEventListener('DOMContentLoaded', () => {
    const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

    $navbarBurgers.forEach(el => {
        el.addEventListener('click', () => {
            const target = el.dataset.target;
            const $target = document.getElementById(target);
            el.classList.toggle('is-active');
            $target.classList.toggle('is-active');
        });
    });
    const themeToggle = document.getElementById('theme-toggle');
    const body = document.documentElement;
    const themes = ['light', 'dark', 'system'];
    let currentTheme = 0;

    function setTheme() {
        body.classList.remove('theme-light', 'theme-dark');
        if (themes[currentTheme] === 'dark') {
            body.classList.add('theme-dark');
        } else if (themes[currentTheme] === 'light') {
            body.classList.add('theme-light');
        } else if (themes[currentTheme] === 'system') {
            // Utilize o tema de preferência do sistema
            const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
            body.classList.add(prefersDark ? 'theme-dark' : 'theme-light');
        }
    }

    themeToggle.addEventListener('click', () => {
        console.log('Testando essa bang')
        currentTheme = (currentTheme + 1) % themes.length;
        setTheme();
    });

    setTheme(); // Definir tema inicial ao carregar a página
});
