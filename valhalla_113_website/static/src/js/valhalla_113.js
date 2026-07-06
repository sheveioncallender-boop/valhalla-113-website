(function () {
    'use strict';

    function ready(callback) {
        if (document.readyState !== 'loading') {
            callback();
        } else {
            document.addEventListener('DOMContentLoaded', callback);
        }
    }

    ready(function () {
        var page = document.querySelector('.v113-page');
        if (!page) {
            return;
        }

        document.body.classList.add('v113-active-page');

        var burger = page.querySelector('.v113-burger');
        var nav = page.querySelector('.v113-nav');
        var header = page.querySelector('.v113-header');

        if (burger && nav) {
            burger.addEventListener('click', function () {
                var isOpen = page.classList.toggle('v113-menu-open');
                burger.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
            });

            nav.querySelectorAll('a').forEach(function (link) {
                link.addEventListener('click', function () {
                    page.classList.remove('v113-menu-open');
                    burger.setAttribute('aria-expanded', 'false');
                });
            });
        }

        if (header) {
            window.addEventListener('scroll', function () {
                if (window.scrollY > 20) {
                    header.classList.add('v113-scrolled');
                } else {
                    header.classList.remove('v113-scrolled');
                }
            }, { passive: true });
        }
    });
})();
