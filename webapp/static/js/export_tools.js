```javascript
// Export Tools

// Dependencies
import { projectData, designData, analysisData } from './main.js';

// Export Data Function
function exportData() {
    let data = {
        project: projectData,
        design: designData,
        analysis: analysisData
    };

    let dataStr = JSON.stringify(data);
    let dataUri = 'data:application/json;charset=utf-8,'+ encodeURIComponent(dataStr);

    let exportFileDefaultName = 'data.json';

    let linkElement = document.createElement('a');
    linkElement.setAttribute('href', dataUri);
    linkElement.setAttribute('download', exportFileDefaultName);
    linkElement.click();
}

// Event Listener for Export Complete
document.addEventListener('exportComplete', function(e) {
    console.log('Export Complete');
}, false);

export { exportData };
```