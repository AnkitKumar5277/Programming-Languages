// Adding JavaScript to HTML 
// Inline Script (Avoid for Production) 
<script>
    console.log("Hello World");
</script>
// External JS File (Recommended) 
<script src="app.js" defer></script>
// Use defer to ensure scripts run after HTML is parsed.
Use type="module" for ES modules.
<script type="module" src="app.js"></script>
