/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './components/**/*.{js,ts,jsx,tsx}',
    './app/**/*.{js,ts,jsx,tsx}',
    './static/js/**/*.js',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
