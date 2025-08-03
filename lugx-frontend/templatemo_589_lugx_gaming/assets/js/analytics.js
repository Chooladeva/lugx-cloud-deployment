function sendEvent(eventType, extraData = {}) {
    fetch("http://app.lugx.cloud:8080/api/analytics/event", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            event_type: eventType,
            page_url: window.location.pathname,
            scroll_depth: extraData.scrollDepth || 0,
            click_target: extraData.clickTarget || "",
            session_id: localStorage.getItem("session_id") || "guest",
            duration: extraData.duration || 0
        })
    });
}

let sessionStart = Date.now();

// 1. Page View
window.addEventListener("load", () => {
    sendEvent("page_view");
});

// 2. Scroll
window.addEventListener("scroll", () => {
    const scrollDepth = Math.round((window.scrollY / document.body.scrollHeight) * 100);
    sendEvent("scroll", { scrollDepth });
});

// 3. Click Events
document.addEventListener("click", (e) => {
    const id = e.target.id || "";
    const cls = e.target.className || "";

    if (id === "add-to-cart") {
        sendEvent("add_to_cart", { clickTarget: id });
    } else if (cls.includes("category-button")) {
        sendEvent("category_click", { clickTarget: cls });
    } else if (id === "search-btn") {
        sendEvent("search_click", { clickTarget: id });
    }
});

// 4. Track Session Duration (on exit)
window.addEventListener("beforeunload", () => {
    const durationSec = Math.round((Date.now() - sessionStart) / 1000);
    sendEvent("session_duration", { duration: durationSec });
});
