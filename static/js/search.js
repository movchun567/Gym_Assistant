document.getElementById('search').addEventListener('input', function() {
    const searchValue = this.value.toLowerCase();
    const cards = document.querySelectorAll('.grid__item_video');

    cards.forEach(function(card) {
        const trainingName = card.querySelector('input[name="training_name"]').value.toLowerCase();
        if (trainingName.includes(searchValue)) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
});