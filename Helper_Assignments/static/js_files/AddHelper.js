document.addEventListener('DOMContentLoaded', function() {
    var selectField = document.getElementById('select-field');
    var selectText = document.getElementById('button-text');
    var listItems = document.getElementById('list-items');
    var arrowDown = document.querySelector('.arrow-down');
    var Submit = document.getElementById('submit');

    selectField.addEventListener('click', function() {
        if (listItems.style.display === 'block') {
            listItems.style.display = 'none';
            arrowDown.classList.remove('rotate');
        } else {
            listItems.style.display = 'block';
            arrowDown.classList.add('rotate');
        }
    });

    document.querySelectorAll(".out-item").forEach(item => {
        item.addEventListener("click", () => {
            selectText.innerHTML = item.querySelector('.out-text').textContent;
            document.getElementById('skill').value = item.querySelector('.out-text').textContent;
            console.log('Skill selected:', item.querySelector('.out-text').textContent); 
            listItems.style.display = 'none';
            arrowDown.classList.remove('rotate');
        });
    });
});
