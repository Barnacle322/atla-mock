// This file simulates a web frontend.
// It generates HTML-like strings based on static data.

// This fake function simulates fetching data from an API
function fetchDashboardData() {
    console.log("Fetching data from API...");
    // Return some static objects
    return [
        { title: "Revenue", value: "$5,000" },
        { title: "New Users", value: "120" },
        { title: "Active Sessions", value: "45" },
    ];
}

// This function "renders" the page to the console
function renderPage() {
    console.log("<html>");
    console.log("  <body>");
    console.log("    <h1>Admin Dashboard</h1>");
    console.log("    <div class='stats'>");

    // Get the data
    var stats = fetchDashboardData();

    // simple loop (no map/filter/reduce to keep it simple)
    for (var i = 0; i < stats.length; i++) {
        var stat = stats[i];
        console.log("      <div class='card'>");
        console.log("        <h2>" + stat.title + "</h2>");
        console.log("        <p>" + stat.value + "</p>");
        console.log("      </div>");
    }

    console.log("    </div>");
    console.log("  </body>");
    console.log("<footer class='footer'>Copyright 2024</footer>")
    console.log("</html>");
}

// Run the render function
renderPage();
