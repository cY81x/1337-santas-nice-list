function createSnowflake() {
    const snowflake = document.createElement('div');
    snowflake.classList.add('snowflake');
    snowflake.textContent = '❄️';
    snowflake.style.left = Math.random() * window.innerWidth + 'px';
    snowflake.style.opacity = Math.random();
    snowflake.style.fontSize = Math.random() * 20 + 10 + 'px';
    
    document.body.appendChild(snowflake);

    let pos = -20; // Start just above the viewport
    const fallSpeed = Math.random() * 2 + 1;
    function fall() {
        if (pos > window.innerHeight) {
            snowflake.remove();
        } else {
            pos += fallSpeed;
            snowflake.style.top = pos + 'px';
            requestAnimationFrame(fall);
        }
    }
    fall();
}

setInterval(createSnowflake, 75);

document.addEventListener('DOMContentLoaded', function () {
    var scrollText = ""
    // JavaScript code to fetch the scroll text from the Flask API
    fetch('/api/scrolltext')
        .then(response => response.json())
        .then(data => {
        scrollText = data.scroll_text;
    })
    .catch(error => {
        console.error('Error fetching scroll text:', error);
    });

    const scrollerElement = document.createElement('div');
    scrollerElement.classList.add('sinus-scroller');
    document.body.appendChild(scrollerElement);

    let offset = 0;
    let xSpeed = 0.15;

    function animate() {
        let output = "";
        for (let i = 0; i < scrollText.length; i++) {
            const xPos = i - offset + 50;
            const yPos = Math.sin((xPos * 0.2) + (Date.now() / 1000)) * 200;
            const char = scrollText[i];

            output += `<span style='transform: translate(${xPos * 25}px, ${yPos}px); color: blue;'>${char}</span>`;
        }

        scrollerElement.innerHTML = output;
        offset += xSpeed;

        if (offset > scrollText.length + 80) {
            offset = 0;
        }

        requestAnimationFrame(animate);
    }

    animate();
});



