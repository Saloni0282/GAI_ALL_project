const express = require('express');
const axios = require('axios');
const cors = require('cors');
const { Octokit } = require("@octokit/rest");
const fetch = (...args) => import('node-fetch').then(({ default: fetch }) => fetch(...args));
require('dotenv').config();
const app = express();
const port = process.env.port || 3000;
app.use(cors());
app.use(express.json());

const CLIENT_ID = process.env.CLIENT_ID
const CLIENT_SECRET = process.env.CLIENT_SECRET
app.get("/", (req, res) => {
    res.json({ data: "Backend Github" })
})
app.get("/get", async (req, res) => {
    console.log(req.query.code);
    const params = "?client_id=" + CLIENT_ID + "&client_secret=" + CLIENT_SECRET + "&code=" + req.query.code + "&scope=repo";
    await fetch("https://github.com/login/oauth/access_token" + params, {
        method: "POST",
        headers: {
            "Accept": "application/json"
        }
    }).then((res) => res.json()).then((data) => {
        res.json(data)
    })
})

app.post("/pushcode", async (req, res) => {
    const { accessToken, brandName, fileContent, fileName, owner, repo, commitMessage } = req.body;
    const octokit = new Octokit({
        auth: accessToken,
    });

    try {
        // Get the current commit SHA for the default branch
        const { data: branchData } = await octokit.repos.getBranch({
            owner,
            repo,
            branch: brandName, // Replace with your default branch name
        });

        // Get the latest commit on the branch
        const latestCommitSha = branchData.commit.sha;

        // Get the current tree of the latest commit
        const { data: treeData } = await octokit.git.getTree({
            owner,
            repo,
            tree_sha: latestCommitSha,
            recursive: true,
        });

        // Find the file if it already exists in the tree
        const file = treeData.tree.find((item) => item.path === fileName);

        if (file) {
            // If the file exists, update it
            await octokit.repos.createOrUpdateFileContents({
                owner,
                repo,
                path: fileName,
                message: `${commitMessage}`,
                content: Buffer.from(fileContent).toString("base64"),
                sha: file.sha,
                branch: brandName, // Replace with your default branch name
            });
        } else {
            // If the file doesn't exist, create it
            await octokit.repos.createOrUpdateFileContents({
                owner,
                repo,
                path: fileName,
                message: `${commitMessage}`,
                content: Buffer.from(fileContent).toString("base64"),
                branch: brandName, // Replace with your default branch name
            });
        }

        console.log(`File "${fileName}" created/updated successfully!`);
        res.json({ isSuccess: true })
    } catch (error) {
        console.error("Error:", error.message);
        res.status(404).json({ isSuccess: false });
    }
})


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
        const prompt = `Debug the following code: ${code}`
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
