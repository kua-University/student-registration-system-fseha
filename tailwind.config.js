/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './main_app/templates/**/*.html'
  ],
  theme: {
    extend: {
      backgroundImage: {
        'hero-pattern': "url('/img/background.jpg')",
        'footer-texture': "url('/img/footer-texture.png')",
      }
    },
  },
  plugins: [],
}

