// script.js
document.addEventListener('DOMContentLoaded', () => {
    const codeInput = document.getElementById('codeInput');
    const targetLanguageSelect = document.getElementById('targetLanguage');
    const convertButton = document.getElementById('convertButton');
    const debugButton = document.getElementById('debugButton');
    const qualityCheckButton = document.getElementById('qualityCheckButton');
    const output = document.getElementById('output');
    const loader = document.getElementById('loader');

    const apiUrl = 'https://code-converter-id3p.onrender.com'; // Update with your backend server URL

    // Clear button functionality
    document.getElementById('clearButton').addEventListener('click', () => {
        codeInput.value = ''; // Clear the textarea
        output.textContent =''; //Clear the textarea
    });

    function clearOutput() {
        output.textContent = '';
    }

    convertButton.addEventListener('click', async () => {
        clearOutput();
        loader.style.display = 'inline-block';
        const code = codeInput.value;
        const targetLanguage = targetLanguageSelect.value;
        
        try {
            const response = await fetch(`${apiUrl}/convert`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ code, targetLanguage }),
            });

            const data = await response.json();
            output.textContent = data.convertedCode;
        } catch (error) {
            console.error('Error converting code:', error);
            output.textContent = 'Code conversion failed.';
        }
    });

    debugButton.addEventListener('click', async () => {
        clearOutput();
        const code = codeInput.value;

        try {
            const response = await fetch(`${apiUrl}/debug`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ code }),
            });

            const data = await response.json();
            output.textContent = data.debuggingOutput;
        } catch (error) {
            console.error('Error debugging code:', error);
            output.textContent = 'Code debugging failed.';
        }
    });

    qualityCheckButton.addEventListener('click', async () => {
        clearOutput();
        const code = codeInput.value;

        try {
            const response = await fetch(`${apiUrl}/check-quality`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ code }),
            });

            const data = await response.json();
            output.textContent = data.qualityAssessment;
        } catch (error) {
            console.error('Error checking code quality:', error);
            output.textContent = 'Code quality check failed.';
        }
    });
});
