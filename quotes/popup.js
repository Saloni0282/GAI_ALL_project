function getQuote() {
    const quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "In the end, we will remember not the words of our enemies, but the silence of our friends. - Martin Luther King, Jr.",
        "Be Yourself; everyone else is alredy taken. - Oscar Wilde"
    ];
    const index = Math.floor(Math.random() * quotes.length);
    return quotes[randomIndex];
}

document.addEventListener('DOMContentLoaded', function () {
    const quoteElement= document.getElementById('quote');
    const newQuoteButton = document.getElementById("new-quote");
    newQuoteButton.addEventListener("click", function () {
        const quote = getQuote();
        quoteElement.textContent = quote;
    })
});
