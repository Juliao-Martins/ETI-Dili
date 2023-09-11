const left = document.querySelectorAll('.left');
const right = document.querySelectorAll('.right');

const observer = new IntersectionObserver(entries => {

  entries.forEach(entry => {

    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    } else {

      setTimeout(() => {

        left.forEach(div => div.classList.add('visible'));
        right.forEach(div => div.classList.add('visible'));
        observer.unobserve(entry.target);

      }, 3000);

    }

  });

}, {
  root: null,
  threshold: 0,
  rootMargin: "-150px"
});


left.forEach(div => observer.observe(div));
right.forEach(div => observer.observe(div));