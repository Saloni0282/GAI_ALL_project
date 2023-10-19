const express = require('express');
const axios = require('axios');
const cors = require('cors');
require('dotenv').config();
const app = express();
const port = process.env.port||3000;
app.use(cors());
app.use(express.json());

app.post('/convert', async (req, res) => {
    const code = req.body.code;
    const targetLanguage = req.body.targetLanguage;

    try {
        const prompt = `Translate the following code into ${targetLanguage}: ${code}`;

        // Make a request to the ChatGPT API to convert the code
        const response = await axios.post('https://api.openai.com/v1/chat/completions', {
            model: 'gpt-3.5-turbo',
            temperature: 0.5,
            max_tokens: 280, // Adjust this based on your needs
            messages: [{
                role: 'system',

                content: 'You are a code convertor in hi.'
            }, { role: 'user', content: prompt }],
        }, {
            headers: {
                'Authorization': `Bearer ${process.env.GPT3_API_KEY}`, // Replace with your API key
                'Content-Type': 'application/json',
            },
        });
        console.log(response.data)
        const convertedCode = response.data.choices[0].message.content;

        res.json({ convertedCode });

    } catch (error) {
        console.error('Error converting code:', error);
        res.status(500).json({ error: 'Code conversion failed.' });
    }
});

app.post('/debug', async (req, res) => {
    const code = req.body.code;

    try {
        const prompt= `Debug the following code: ${code}`
        // Make a request to the ChatGPT API for code debugging
        const response = await axios.post('https://api.openai.com/v1/chat/completions', {
           
            model: 'gpt-3.5-turbo',
            temperature: 0.5,
            max_tokens: 280, // Adjust this based on your needs
            messages: [{
                role: 'system',

                content: 'You are a code debuger in hi.'
            }, { role: 'user', content: prompt }],
        }, {
            headers: {
                'Authorization': `Bearer ${process.env.GPT3_API_KEY}`, // Replace with your API key
                'Content-Type': 'application/json',
            },
        });

        const debuggingOutput = response.data.choices[0].message.content;

        res.json({ debuggingOutput });
    } catch (error) {
        console.error('Error debugging code:', error);
        res.status(500).json({ error: 'Code debugging failed.' });
    }
});

app.post('/check-quality', async (req, res) => {
    const code = req.body.code;

    try {
        const qualityParameters = [
            'Code Consistency',
            'Code Performance',
            'Code Documentation',
            'Error Handling',
            'Code Testability',
            'Code Modularity',
            'Code Complexity',
            'Code Duplication',
            'Code Readability'
        ];
        const prompt = `Evaluate the quality of the following code based on the following parameters: ${qualityParameters.join(', ')}\n\n${code}`;

        // const prompt= `Check the quality of the following code: ${code}`
        // Make a request to the ChatGPT API for code quality assessment
        const response = await axios.post('https://api.openai.com/v1/chat/completions', {
            
            model: 'gpt-3.5-turbo',
            temperature: 0.5,
            max_tokens: 300, // Adjust this based on your needs
            messages: [{
                role: 'system',

                content: 'You are a code quality evaluator.'
            }, { role: 'user', content: prompt }],
        }, {
            headers: {
                'Authorization': `Bearer ${process.env.GPT3_API_KEY}`, // Replace with your API key
                'Content-Type': 'application/json',
            },
        });

        const qualityAssessment = response.data.choices[0].message.content;

        res.json({ qualityAssessment });
    } catch (error) {
        console.error('Error checking code quality:', error);
        res.status(500).json({ error: 'Code quality check failed.' });
    }
});


// Other routes and middleware

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
