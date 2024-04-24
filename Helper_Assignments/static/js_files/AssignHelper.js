document.addEventListener('DOMContentLoaded', function() {
    var selectField = document.getElementById('select-field');
    var selectText = document.getElementById('button-text');
    var listItems = document.getElementById('list-items');
    var arrowDown = document.querySelector('.arrow-down');
    var Submit = document.getElementById('submit');
    var helperSelect = document.getElementById('helper')
    

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
            listItems.style.display = 'none';
            arrowDown.classList.remove('rotate');

            document.getElementById('skill').value = item.querySelector('.out-text').textContent;
            console.log('Skill selected:', item.querySelector('.out-text').textContent); 

            // Show helpers of selected skill
            var selectedSkill = item.querySelector('.out-text').textContent;
            var helpers = document.querySelectorAll('#helper option');
            helpers.forEach(helper => {
                if (helper.getAttribute('data-skill') === selectedSkill) {
                    helper.style.display = 'block';
                } else {
                    helper.style.display = 'none';
                }
            });     
        });
    });
});
