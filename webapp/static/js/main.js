```javascript
// Importing dependencies
import { setupProject } from './project_wizard.js';
import { generateDesign } from './ai_engine.js';
import { analyzeDesign } from './design_analysis.js';
import { exportData } from './export_tools.js';
import { updateUI } from './3d_viewer.js';
import { handleError } from './exceptions.js';

// Global variables
let projectData = null;
let userData = null;
let designData = null;
let analysisData = null;

// DOM elements
const projectSetupForm = document.getElementById('projectSetupForm');
const designViewContainer = document.getElementById('designViewContainer');
const analysisViewContainer = document.getElementById('analysisViewContainer');
const exportViewContainer = document.getElementById('exportViewContainer');

// Event listeners
projectSetupForm.addEventListener('submit', (event) => {
    event.preventDefault();
    try {
        projectData = setupProject(event.target);
        updateUI(designViewContainer, projectData);
    } catch (error) {
        handleError(error);
    }
});

designViewContainer.addEventListener('projectSetupComplete', () => {
    try {
        designData = generateDesign(projectData);
        updateUI(analysisViewContainer, designData);
    } catch (error) {
        handleError(error);
    }
});

analysisViewContainer.addEventListener('designGenerated', () => {
    try {
        analysisData = analyzeDesign(designData);
        updateUI(exportViewContainer, analysisData);
    } catch (error) {
        handleError(error);
    }
});

exportViewContainer.addEventListener('analysisComplete', () => {
    try {
        exportData(analysisData);
    } catch (error) {
        handleError(error);
    }
});
```