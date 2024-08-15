document.addEventListener('DOMContentLoaded', () => {
    const subjects = document.querySelectorAll('.subjects');

    subjects.forEach((subject) => {
        subject.addEventListener('click', () => {
            subjects.forEach(s => s.classList.remove('active'));

            if (!subject.classList.contains('active')) {
                subject.classList.add('active');
            }
        });
    });
});
