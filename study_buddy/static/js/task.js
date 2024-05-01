document.addEventListener('DOMContentLoaded', function() {
    const pairs = document.querySelectorAll('.pair');
    const allElements = Array.from(document.querySelectorAll('.element'));

    shuffleElements(allElements);

    let index = 0;
    pairs.forEach(pair => {
        const elements = Array.from(pair.querySelectorAll('.element'));

        pair.innerHTML = '';

        elements.forEach(element => {
            if (index < allElements.length) {
                const selectedElement = allElements[index].cloneNode(true);
                if (selectedElement.dataset.image) {
                    const image = document.createElement('img');
                    image.src = selectedElement.dataset.image;
                    selectedElement.innerHTML = '';
                    selectedElement.appendChild(image);
                }
                pair.appendChild(selectedElement);
                index++;
            }
        });
    });

    const elements = document.querySelectorAll('.element');
    let selectedElement = null;
    let correctPairs = 0;
    let totalPairs = 0;

    elements.forEach(element => {
        element.addEventListener('click', () => {
            if (!selectedElement) {
                selectedElement = element;
                element.classList.add('selected');
            } else {
                if (element !== selectedElement && element.dataset.id === selectedElement.dataset.id) {           
                    element.style.display = 'none';
                    selectedElement.style.display = 'none';
                    correctPairs++;
                    totalPairs++;
                    updateResults();
                } else {
                    selectedElement.classList.remove('selected');
                    totalPairs++;
                    updateResults();
                }
                selectedElement = null;
            }
        });
    });

    function updateResults() {
        const resultElement = document.getElementById('results');
        resultElement.textContent = `Правильно: ${correctPairs}, Неправильно: ${totalPairs - correctPairs}`;
    }

    function shuffleElements(elements) {
        for (let i = elements.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [elements[i], elements[j]] = [elements[j], elements[i]];
        }
    }
});
