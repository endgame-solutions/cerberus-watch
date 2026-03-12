/**
 * Cerberus Dashboard JavaScript
 * Main functionality for the Cerberus dashboard
 */

// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize the dashboard
    initDashboard();
    
    // Set up event listeners
    setupEventListeners();
    
    // Check for admin access
    checkAdminAccess();
});

/**
 * Initialize the dashboard components
 */
function initDashboard() {
    console.log('Initializing Cerberus Dashboard...');
    
    // Update stats with random data (for demo purposes)
    updateStats();
    
    // Check authentication status
    checkAuthStatus();
}

/**
 * Set up event listeners for interactive elements
 */
function setupEventListeners() {
    // Mobile sidebar toggle
    const sidebarToggle = document.getElementById('sidebar-toggle');
    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', function() {
            const sidebar = document.querySelector('.sidebar');
            sidebar.classList.toggle('active');
        });
    }
    
    // Login form submission
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', function(e) {
            e.preventDefault();
            handleLogin();
        });
    }
    
    // Logout button
    const logoutBtn = document.getElementById('logout-btn');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', function(e) {
            e.preventDefault();
            handleLogout();
        });
    }
    
    // Admin access code input
    const adminCodeInput = document.getElementById('admin-code');
    if (adminCodeInput) {
        adminCodeInput.addEventListener('input', function() {
            checkAdminCode(this.value);
        });
    }
}

/**
 * Update dashboard statistics with random data
 * In a real implementation, this would fetch data from an API
 */
function updateStats() {
    // Get all stat value elements
    const statValues = document.querySelectorAll('.stat-value');
    
    // Update each stat with a random value
    statValues.forEach(function(stat) {
        const dataType = stat.getAttribute('data-type');
        let value;
        
        switch (dataType) {
            case 'integer':
                value = Math.floor(Math.random() * 1000);
                break;
            case 'percentage':
                value = Math.floor(Math.random() * 100) + '%';
                break;
            case 'decimal':
                value = (Math.random() * 100).toFixed(2);
                break;
            default:
                value = Math.floor(Math.random() * 100);
        }
        
        stat.textContent = value;
    });
    
    console.log('Stats updated');
}

/**
 * Check if user is authenticated
 */
function checkAuthStatus() {
    const isAuthenticated = localStorage.getItem('cerberus_authenticated');
    const loginRequired = document.body.classList.contains('login-required');
    
    if (loginRequired && !isAuthenticated) {
        // Redirect to login page if not authenticated
        if (!window.location.pathname.includes('login.html')) {
            window.location.href = 'login.html';
        }
    } else if (isAuthenticated && window.location.pathname.includes('login.html')) {
        // Redirect to dashboard if already authenticated
        window.location.href = 'index.html';
    }
}

/**
 * Handle login form submission
 */
function handleLogin() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    // Simple validation
    if (!username || !password) {
        showAlert('Please enter both username and password', 'danger');
        return;
    }
    
    // In a real implementation, this would make an API call
    // For demo purposes, accept any non-empty credentials
    localStorage.setItem('cerberus_authenticated', 'true');
    localStorage.setItem('cerberus_username', username);
    
    // Redirect to dashboard
    window.location.href = 'index.html';
}

/**
 * Handle logout
 */
function handleLogout() {
    localStorage.removeItem('cerberus_authenticated');
    localStorage.removeItem('cerberus_username');
    localStorage.removeItem('cerberus_admin');
    
    // Redirect to login page
    window.location.href = 'login.html';
}

/**
 * Show an alert message
 */
function showAlert(message, type = 'info') {
    const alertContainer = document.getElementById('alert-container');
    if (!alertContainer) return;
    
    const alert = document.createElement('div');
    alert.className = `alert alert-${type}`;
    alert.textContent = message;
    
    // Add close button
    const closeBtn = document.createElement('button');
    closeBtn.className = 'close';
    closeBtn.innerHTML = '&times;';
    closeBtn.addEventListener('click', function() {
        alert.remove();
    });
    
    alert.appendChild(closeBtn);
    alertContainer.appendChild(alert);
    
    // Auto-remove after 5 seconds
    setTimeout(function() {
        alert.remove();
    }, 5000);
}

/**
 * Check for admin access code
 * Now validates securely via backend API
 */
async function checkAdminCode(code) {
    if (!code) return;

    try {
        const response = await fetch('/api/verify-admin', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ code: code })
        });

        if (response.ok) {
            const result = await response.json();
            if (result.success) {
                localStorage.setItem('cerberus_admin', 'true');
                showAdminPanel();
            }
        }
    } catch (error) {
        console.error('Error verifying admin code:', error);
    }
}

/**
 * Check if user has admin access
 */
function checkAdminAccess() {
    const isAdmin = localStorage.getItem('cerberus_admin') === 'true';
    
    if (isAdmin) {
        showAdminPanel();
    }
}

/**
 * Show the admin panel
 */
function showAdminPanel() {
    const adminPanel = document.querySelector('.admin-panel');
    if (adminPanel) {
        adminPanel.classList.add('visible');
    }
    
    const adminNavItem = document.getElementById('admin-nav-item');
    if (adminNavItem) {
        adminNavItem.style.display = 'block';
    }
    
    console.log('Admin access granted');
}

/**
 * Initialize charts (placeholder for chart implementation)
 */
function initCharts() {
    console.log('Charts would be initialized here');
    // In a real implementation, this would create charts using a library like Chart.js
}
