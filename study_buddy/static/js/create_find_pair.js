var pairCounter = 0; 

function addPair() {
    pairCounter++;
    var pairDiv = document.createElement('div');
    pairDiv.id = 'pair_' + pairCounter;
    pairDiv.className = 'pair';
    pairDiv.innerHTML = `
        <label for="pair_${pairCounter}_first_type">Выберите тип первого элемента пары:</label><br>
        <select id="pair_${pairCounter}_first_type" onchange="toggleInput(${pairCounter}, 'first')">
            <option value="text">Текст</option>
            <option value="image">Изображение</option>
        </select><br>

        <div id="pair_${pairCounter}_first_text_input">
            <input type="text" id="pair_${pairCounter}_first_text" name="pair_${pairCounter}_first_text" placeholder="Введите текст">
        </div>
        <div id="pair_${pairCounter}_first_image_input" style="display:none;">
            <input type="file" id="pair_${pairCounter}_first_image" name="pair_${pairCounter}_first_image">
        </div>
        <br>

        <label for="pair_${pairCounter}_second_type">Выберите тип второго элемента пары:</label><br>
        <select id="pair_${pairCounter}_second_type" onchange="toggleInput(${pairCounter}, 'second')">
            <option value="text">Текст</option>
            <option value="image">Изображение</option>
        </select><br>

        <div id="pair_${pairCounter}_second_text_input">
            <input type="text" id="pair_${pairCounter}_second_text" name="pair_${pairCounter}_second_text" placeholder="Введите текст">
        </div>
        <div id="pair_${pairCounter}_second_image_input" style="display:none;">
            <input type="file" id="pair_${pairCounter}_second_image" name="pair_${pairCounter}_second_image">
        </div>
        <button type="button" class="remove-pair-btn" onclick="removePair(${pairCounter})">Удалить пару</button>
        <hr>
    `;
    document.getElementById('pairs_container').appendChild(pairDiv);
}

function toggleInput(pairIndex, element) {
    var typeSelect = document.getElementById(`pair_${pairIndex}_${element}_type`);
    var textInput = document.getElementById(`pair_${pairIndex}_${element}_text_input`);
    var imageInput = document.getElementById(`pair_${pairIndex}_${element}_image_input`);

    if (typeSelect.value === 'text') {
        textInput.style.display = 'block';
        imageInput.style.display = 'none';
        document.getElementById(`pair_${pairIndex}_${element}_image`).value = '';
    } else if (typeSelect.value === 'image') {
        textInput.style.display = 'none';
        imageInput.style.display = 'block';
        document.getElementById(`pair_${pairIndex}_${element}_text`).value = '';
    }
}

function removePair(pairCounter) {
    var pairDiv = document.getElementById('pair_' + pairCounter);
    pairDiv.remove();
    pairCounter--; 
}

function validateForm() {
    var pairs = document.querySelectorAll('[id^="pair_"]');
    var title = document.getElementById('task_title').value.trim();
    var description = document.getElementById('task_description').value.trim();

    if (title === '') {
        alert('Пожалуйста, введите название задания.');
        return false;
    }

    if (description === '') {
        alert('Пожалуйста, введите описание задания.');
        return false;
    }

    var hasAtLeastOnePair = false;
    for (var i = 0; i < pairs.length; i++) {
        var pair = pairs[i];
        var firstTypeElement = pair.querySelector('[id$="_first_type"]');
        var firstType = firstTypeElement ? firstTypeElement.value : '';
        var firstValueElement = pair.querySelector('[id$="_first_text"]');
        var firstValue = firstValueElement ? firstValueElement.value.trim() : '';
        var secondTypeElement = pair.querySelector('[id$="_second_type"]');
        var secondType = secondTypeElement ? secondTypeElement.value : '';
        var secondValueElement = pair.querySelector('[id$="_second_text"]');
        var secondValue = secondValueElement ? secondValueElement.value.trim() : '';

        if ((firstType === 'text' && firstValue === '') || (secondType === 'text' && secondValue === '')) {
            alert('Пожалуйста, заполните все текстовые поля в каждой паре.');
            return false;
        }

        if (firstType === 'image' && pair.querySelector('[id$="_first_image"]').value === '') {
            alert('Пожалуйста, загрузите изображение для первого элемента в каждой паре.');
            return false;
        }
        if (secondType === 'image' && pair.querySelector('[id$="_second_image"]').value === '') {
            alert('Пожалуйста, загрузите изображение для второго элемента в каждой паре.');
            return false;
        }

        if (firstValue !== '' || secondValue !== '') {
            hasAtLeastOnePair = true;
        }
    }

    if (!hasAtLeastOnePair) {
        alert('Пожалуйста, создайте хотя бы одну пару.');
        return false;
    }

    return true;
}
