/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../../templates/**/*.{html,js}"],
  plugins: [require("daisyui")],
  theme: {
    extend: {},
  }
}