// const menus = document.querySelectorAll('details[class^="menu-"]');

// for (const menu of menus) {
//     const nls = menu.querySelectorAll('.nl');
//     const _details = menu.querySelectorAll('details');

//     menu.addEventListener('mouseleave', (event) => {
//         menu.removeAttribute('open');
//         for (const detail of _details) detail.removeAttribute('open');
//     });

//     for (const summary of nls) {
//         summary.addEventListener('mouseenter', (event) => {
//             event.target.parentElement.setAttribute('open', '');
//         });

//         summary.addEventListener('mouseleave', (event) => {
//             const childrens = Array.from(event.target.parentElement.getElementsByTagName('*'));
//             const exists = childrens.find(val => val == event.relatedTarget);
//             if (!exists) event.target.parentElement.removeAttribute('open');
//         });
//     };
// };



const container = document.querySelector('.container-menus');
const target = container.querySelector(`a[href="${document.location.pathname}"]`);

if (target) {
    target.style.textDecoration = 'underline';

    let details = target.closest('details');
    details.setAttribute('open', '');

    while (true) {
        const class_list = Array.from(details.classList);
        const exists = class_list.find(val => val.slice(0, 5) === 'menu-');
        if (exists) break;
        details = details.parentElement.closest('details');
        details.setAttribute('open', '');
    };
};
