// class for planet in canvas
class Planet {
    static zoom = 1
    static speed = 1

    constructor(distance, velocity, radius,  imgSrc) {
        this.distance = distance
        this.velocity = velocity
        this.radius = radius
        this.angle = 0
        this.img = new Image()
        this.img.src = imgSrc
    }

    show() {
        ctx.save()
        ctx.beginPath()
        ctx.strokeStyle = 'rgb(50, 50, 50)'
        ctx.arc(0, 0, this.distance * Planet.zoom, 0, Math.PI * 2)
        ctx.lineWidth = 1.5
        ctx.stroke()
        ctx.rotate(this.angle)
        ctx.drawImage(this.img, (this.distance - this.radius) * Planet.zoom, -this.radius * Planet.zoom, this.radius * 2 * Planet.zoom, this.radius * 2 * Planet.zoom)
        this.angle += this.velocity / 100 * Planet.speed
        ctx.restore()
    }
}

// looped function drawing solar system in canvas
function draw() {
    ctx.fillStyle = 'rgba(0, 0, 0)'
    ctx.fillRect(0, 0, canvas.width, canvas.height)
    ctx.save()

    ctx.translate(center.x, center.y)
    sun.show()

    for(let planet of planets) {
        planet.show()
    }

    ctx.restore()
    requestAnimationFrame(draw)
}

// canvas
const canvas = document.getElementById("canvas")
const ctx = canvas.getContext("2d")
const width = canvas.width
const height = canvas.height
const center = {
    x: canvas.width / 2,
    y: canvas.height / 2
}

// load images
const prefix = 'static/assets/'
const sun = new Planet(0, 0, 40, prefix + 'sun.png')
const planets = [
    new Planet(70, 1 / 0.2408, 7, prefix + 'mercury.png'),
    new Planet(100, 1 / 0.6152, 12, prefix + 'venus.png'),
    new Planet(140, 1, 14, prefix + 'earth.png'),
    new Planet(185, 1 / 1.8808, 10, prefix + 'mars.png'),
    new Planet(265, 1 / 11.8637, 34, prefix + 'jupiter.png'),
    new Planet(340, 1 / 29.4484, 42, prefix + 'saturn.png'),
    new Planet(400, 1 / 84.0711, 20, prefix + 'uranus.png'),
    new Planet(460, 1 / 164.8799, 20, prefix + 'neptune.png')
]

// check if all images are loaded
let loadedImageCount = 0
planets.forEach(planet => {
     planet.img.onload = () => {
         loadedImageCount += 1;
         if(loadedImageCount === planets.length){
             requestAnimationFrame(draw)
         }
     }
});

// range inputs
const zoom = document.getElementById('zoom')
const zoomValue = document.getElementById('zoom-value')
const speed = document.getElementById('speed')
const speedValue = document.getElementById('speed-value')

zoom.addEventListener('change', e => {
    Planet.zoom = e.target.value / 100
    zoomValue.innerHTML = Planet.zoom
})

speed.addEventListener('change', e => {
    Planet.speed = e.target.value / 100
    speedValue.innerHTML = Planet.speed
})