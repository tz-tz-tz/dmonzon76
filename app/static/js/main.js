const btnDelete = document.querySelectorAll('btn-delete')

if (btnDelete) {
    const btnArray = Array.from(btnDelete);
    btnArray.forEach((btn) => {
        btn.addEventListener('click', () => {
            if (confirm('Are yuo sure you want to delete it?')) {
                e.preventDefault();
            }
        });
    });

}