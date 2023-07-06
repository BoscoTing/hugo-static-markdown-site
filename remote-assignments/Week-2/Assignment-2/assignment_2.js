var headUpdate = document.querySelector('h1');
headUpdate.addEventListener('click', () => {
    headUpdate.textContent = 'Have a Good Time!';
})

const showBoxContent = document.querySelector('.hidden_content_box');
const callToAction = document.querySelector('.action');
showBoxContent.style.display = 'none';

callToAction.addEventListener('click', () => {
    if (showBoxContent.style.display === 'none') {
        showBoxContent.removeAttribute('style');
    } else {
        showBoxContent.style.display = 'none';
    }
});

