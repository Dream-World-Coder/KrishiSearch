document.addEventListener('DOMContentLoaded', ()=>{
    const menuBtns = document.querySelectorAll('.options');
    const homePage = document.querySelector('.main__message');
    const searchResult = document.querySelector('.search__reasults');
    const profile = document.querySelector('.profile');
    const news = document.querySelector('.news');
    const header = document.querySelector('header');
    const main = document.querySelector('main');

    // all these nodes are initially hidden
    const pagesArray = [news, homePage, searchResult, profile];

    function highlightMenu(idx){
        menuBtns.forEach((menu, index) => {
            if(index !== idx && menu.classList.contains('menu_activated')){
                menu.classList.remove('menu_activated');
            }
        });
        menuBtns[idx].classList.add('menu_activated');
    }

    function hidePages(idx){
        pagesArray.forEach((page,index)=>{
            if(index!==idx){
                page.style.display = 'none';
            }
        });
    }

    // one menu will be activated at first in the beginning
    pagesArray.forEach((page,index)=>{
        if(index<2 && !page.classList.contains('hidden')){
            highlightMenu(index);
        }
        if(index > 2 && !page.classList.contains('hidden')){
            highlightMenu(index-1)
        }
    })

    // 0 --> news , 1 --> search, 2 --> profile
    menuBtns[0].addEventListener('click', ()=>{
        // make the other pages hidden except index=0
        hidePages(0);

        // make the current page visible
        if(pagesArray[0].classList.contains('hidden')){
            pagesArray[0].classList.remove('hidden');
        }
        pagesArray[0].style.display = 'flex';
        // highlight the menu button for current page
        highlightMenu(0);
    });

    menuBtns[1].addEventListener('click', ()=>{
        hidePages(1);
        if(pagesArray[1].classList.contains('hidden')){
            pagesArray[1].classList.remove('hidden');
        }
        pagesArray[1].style.display = 'flex';
        highlightMenu(1);
    });

    menuBtns[2].addEventListener('click', ()=>{
        hidePages(3);
        if(pagesArray[3].classList.contains('hidden')){
            pagesArray[3].classList.remove('hidden');
        }
        pagesArray[3].style.display = 'flex';
        highlightMenu(2);
    });




    const observer = new MutationObserver(() => {
        if (window.getComputedStyle(profile).display !== 'none') {
            header.style.display = 'none';
            main.style.height = '90dvh';
            // profile.querySelectorAll('*').forEach(el => el.style.display = 'flexbox');
        } else {
            header.style.display = 'flex';
            main.style.height = '80dvh';
            // profile.querySelectorAll('*').forEach(el => el.style.display = 'none');
        }
    });
    
    observer.observe(profile, { attributes: true, attributeFilter: ['style'] });
    
    if (window.getComputedStyle(profile).display !== 'none') {
        header.style.display = 'none';
        main.style.height = '90dvh';
        // profile.querySelectorAll('*').forEach(el => el.style.display = 'flexbox');
    } else {
        header.style.display = 'flex';
        main.style.height = '80dvh';
        // profile.querySelectorAll('*').forEach(el => el.style.display = 'none');
    }
    
});