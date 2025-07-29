---
layout: about  
image: /assets/img/blog/hydejack-9.jpg  
hide_description: true  
redirect_from:  
  - /resume/  
---

<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GitHub Profile Page</title>
    <style>
        /* Reset and Base Styles */  
        * {  
            margin: 0;  
            padding: 0;  
            box-sizing: border-box;  
        }  

        /* CSS Variables from Design System */  
        :root {  
            /* Colors */  
            --color-neutral-0: #ffffff;  
            --color-neutral-1: #f6f8fa;  
            --color-neutral-2: #f1f3f4;  
            --color-neutral-3: #d0d7de;  
            --color-neutral-4: #afb8c1;  
            --color-neutral-5: #8c959f;  
            --color-neutral-6: #6e7781;  
            --color-neutral-7: #656d76;  
            --color-neutral-8: #24292f;  

            --color-accent-primary: #0969da;  
            --color-accent-secondary: #0550ae;  
            --color-success-primary: #1a7f37;  
            --color-success-secondary: #238636;  
            --color-attention-primary: #bf8700;  
            --color-orange-primary: #fd7e14;  

            --color-text-primary: #24292f;  
            --color-text-secondary: #656d76;  
            --color-text-muted: #6e7781;  
            --color-text-link: #0969da;  
            --color-text-link-hover: #0550ae;  

            --color-bg-default: #ffffff;  
            --color-bg-muted: #f6f8fa;  
            --color-bg-subtle: #f1f3f4;  

            --color-border-default: #d0d7de;  
            --color-border-muted: #f1f3f4;  
            --color-border-emphasis: #afb8c1;  

            /* Typography */  
            --font-family-system: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";  

            /* Spacing */  
            --space-1: 4px;  
            --space-2: 8px;  
            --space-3: 12px;  
            --space-4: 16px;  
            --space-5: 20px;  
            --space-6: 24px;  
            --space-8: 32px;  
            --space-10: 40px;  
            --space-12: 48px;  
            --space-16: 64px;  

            /* Borders */  
            --border-radius-small: 3px;  
            --border-radius-medium: 6px;  
            --border-radius-large: 12px;  
            --border-radius-full: 50%;  

            /* Shadows */  
            --shadow-small: 0 1px 3px rgba(0,0,0,0.12);  
            --shadow-medium: 0 1px 3px rgba(0,0,0,0.1);  
            --shadow-focus: 0 0 0 3px rgba(9,105,218,0.3);  

            /* GitHub Contribution Colors */  
            --contrib-bg: #ebedf0;  
            --contrib-level-0: #ebedf0;  
            --contrib-level-1: #9be9a8;  
            --contrib-level-2: #40c463;  
            --contrib-level-3: #30a14e;  
            --contrib-level-4: #216e39;  
        }  

        body {  
            font-family: var(--font-family-system);  
            background-color: var(--color-bg-default);  
            color: var(--color-text-primary);  
            line-height: 1.5;  
            font-size: 16px;  
        }  

        /* Layout */  
        .container {  
            max-width: 1280px;  
            margin: 0 auto;  
            padding: 0 var(--space-6);  
        }  

        .header {  
            background-color: var(--color-neutral-8);  
            color: var(--color-neutral-0);  
            padding: var(--space-4) 0;  
            margin-bottom: var(--space-6);  
        }  

        .header-content {  
            display: flex;  
            align-items: center;  
            justify-content: space-between;  
        }  

        .logo {  
            font-size: 20px;  
            font-weight: 600;  
        }  

        .main-content {  
            display: grid;  
            grid-template-columns: 25% 75%;  
            gap: var(--space-6);  
            margin-bottom: var(--space-16);  
        }  

        /* Sidebar */  
        .sidebar {  
            padding-right: var(--space-6);  
        }  

        .profile-section {  
            margin-bottom: var(--space-8);  
        }  

        .avatar {  
            width: 296px;  
            height: 296px;  
            border-radius: var(--border-radius-full);  
            border: 1px solid var(--color-border-default);  
            background-color: var(--color-bg-muted);  
            display: flex;  
            align-items: center;  
            justify-content: center;  
            font-size: 50px;  
            color: var(--color-text-muted);  
            margin-bottom: var(--space-4);  
            overflow: hidden;  
        }  

        .avatar img {  
            width: 100%;  
            height: 100%;  
            object-fit: cover;  
            object-position: center 20%;  
            border-radius: var(--border-radius-full);  
        }  

        .profile-name {  
            font-size: 28px;  
            font-weight: 600;  
            color: var(--color-text-primary);  
            margin-bottom: var(--space-2);  
        }  

        .profile-stats {  
            margin: var(--space-4) 0;  
        }  

        .stat-item {  
            display: flex;  
            align-items: center;  
            margin-bottom: var(--space-1);  
            font-size: 16px;  
            color: var(--color-text-secondary);  
        }  

        .stat-value {  
            font-size: 16px;  
            color: var(--color-text-primary);  
            margin-bottom: var(--space-3);  
            margin-left: var(--space-6);  
            font-weight: 400;  
        }  

        .profile-link {  
            color: var(--color-text-link);  
            text-decoration: none;  
            transition: color 150ms ease-in-out;  
        }  

        .profile-link:hover {  
            color: var(--color-text-link-hover);  
            text-decoration: underline;  
        }  

        .stat-icon {  
            margin-right: var(--space-2);  
            width: 16px;  
            height: 16px;  
        }  

        /* GitHub Contribution Chart Styles */  
        .contribution-section {  
            margin-top: var(--space-6);  
            padding: var(--space-4);  
            background: var(--color-bg-muted);  
            border: 1px solid var(--color-border-default);  
            border-radius: var(--border-radius-medium);  
        }  

        .contribution-title {  
            font-size: 14px;  
            font-weight: 600;  
            color: var(--color-text-primary);  
            margin-bottom: var(--space-3);  
            display: flex;  
            align-items: center;  
            gap: var(--space-2);  
        }  

        .contribution-calendar {  
            border-spacing: 2px;  
            font-size: 10px;  
            border-collapse: separate;  
        }  

        .contribution-calendar td {  
            padding: 0;  
        }  

        .contrib-day {  
            width: 10px;  
            height: 10px;  
            border-radius: 2px;  
            background-color: var(--contrib-bg);  
        }  

        .contrib-day[data-level="0"] { background-color: var(--contrib-level-0); }  
        .contrib-day[data-level="1"] { background-color: var(--contrib-level-1); }  
        .contrib-day[data-level="2"] { background-color: var(--contrib-level-2); }  
        .contrib-day[data-level="3"] { background-color: var(--contrib-level-3); }  
        .contrib-day[data-level="4"] { background-color: var(--contrib-level-4); }  

        .contrib-month-label {  
            font-size: 10px;  
            color: var(--color-text-muted);  
            text-align: center;  
            padding: 0 var(--space-1);  
        }  

        .contrib-day-label {  
            font-size: 9px;  
            color: var(--color-text-muted);  
            text-align: right;  
            padding-right: var(--space-1);  
            line-height: 10px;  
        }  

        .contrib-legend {  
            display: flex;  
            align-items: center;  
            justify-content: flex-end;  
            margin-top: var(--space-2);  
            font-size: 11px;  
            color: var(--color-text-muted);  
            gap: var(--space-1);  
        }  

        .contrib-legend-item {  
            width: 10px;  
            height: 10px;  
            border-radius: 2px;  
        }  

        /* Main Content Area */  
        .content-area {  
            padding-left: var(--space-6);  
        }  

        .navigation {  
            border-bottom: 1px solid var(--color-border-default);  
            margin-bottom: var(--space-6);  
        }  

        .nav-tabs {  
            display: flex;  
            list-style: none;  
        }  

        .nav-tab {  
            margin-right: var(--space-8);  
        }  

        .nav-tab a {  
            display: block;  
            padding: var(--space-4) 0;  
            color: var(--color-text-secondary);  
            text-decoration: none;  
            font-size: 16px;  
            font-weight: 400;  
            border-bottom: 2px solid transparent;  
            transition: all 150ms ease-in-out;  
        }  

        .nav-tab a:hover {  
            color: var(--color-text-primary);  
        }  

        .nav-tab.active a {  
            color: var(--color-text-primary);  
            border-bottom-color: var(--color-orange-primary);  
            font-weight: 600;  
        }  

        .content-section {  
            margin-bottom: var(--space-8);  
        }  

        /* Grid Resume Layout */  
        .resume-grid {  
            display: grid;  
            grid-template-columns: repeat(2, 1fr);  
            gap: var(--space-4);  
            margin-top: var(--space-4);  
        }  

        .resume-card {  
            background-color: var(--color-bg-default);  
            border: 1px solid var(--color-border-default);  
            border-radius: var(--border-radius-medium);  
            padding: var(--space-4);  
            box-shadow: var(--shadow-small);  
        }  

        .skills-card {  
            grid-column: 1 / -1;  
        }  

        .card-title {  
            font-size: 18px;  
            font-weight: 600;  
            color: var(--color-text-primary);  
            margin-bottom: var(--space-4);  
            border-bottom: 1px solid var(--color-border-muted);  
            padding-bottom: var(--space-2);  
        }  

        .card-content {  
            font-size: 16px;  
        }  

        .item {  
            margin-bottom: var(--space-3);  
        }  

        .item:last-child {  
            margin-bottom: 0;  
        }  

        .item-title {  
            font-weight: 600;  
            color: var(--color-text-primary);  
            margin-bottom: var(--space-1);  
        }  

        .item-desc {  
            color: var(--color-text-secondary);  
            font-size: 15px;  
            margin-bottom: var(--space-1);  
        }  

        .item-skills {  
            color: var(--color-text-muted);  
            font-size: 14px;  
        }  

        .cert-group {  
            margin-bottom: var(--space-4);  
        }  

        .cert-group:last-child {  
            margin-bottom: 0;  
        }  

        .cert-category {  
            font-weight: 600;  
            color: var(--color-text-primary);  
            margin-bottom: var(--space-2);  
        }  

        .cert-items {  
            display: flex;  
            flex-direction: column;  
            gap: var(--space-1);  
        }  

        .cert-items li {  
            color: var(--color-text-secondary);  
            font-size: 15px;  
        }  
        
        .skills-table {  
            width: 100%;  
            border-collapse: collapse;  
            font-size: 15px;  
        }  

        .skills-table th,  
        .skills-table td {  
            padding: var(--space-2) var(--space-3);  
            text-align: left;  
            border-bottom: 1px solid var(--color-border-muted);  
        }  

        .skills-table th {  
            background-color: var(--color-bg-muted);  
            font-weight: 600;  
            color: var(--color-text-primary);  
        }  

        .skills-table td {  
            color: var(--color-text-secondary);  
        }  

        .skill-primary {  
            color: var(--color-accent-primary);  
            font-weight: 600;  
        }  

        /* Project Section Styles */  
        .project-list {  
            display: flex;  
            flex-direction: column;  
            gap: var(--space-4);  
        }  

        .project-card {  
            display: grid;  
            grid-template-columns: 150px 1fr;  
            gap: var(--space-4);  
            border: 1px solid var(--color-border-default);  
            padding: var(--space-4);  
            border-radius: var(--border-radius-medium);  
            box-shadow: var(--shadow-small);  
            align-items: flex-start;  
        }  

        .project-image img {  
            width: 100%;  
            height: auto;  
            border-radius: var(--border-radius-medium);  
            border: 1px solid var(--color-border-muted);  
        }  

        .project-details h3 {  
            font-size: 18px;  
            font-weight: 600;  
            margin-bottom: var(--space-2);  
        }  

        .project-details p {  
            font-size: 15px;  
            color: var(--color-text-secondary);  
            margin-bottom: var(--space-1);  
        }  
        
        .project-links {  
            margin-top: var(--space-3);  
            display: flex;  
            gap: var(--space-4);  
        }  

        .project-link {  
            font-size: 14px;  
            font-weight: 500;  
            color: var(--color-text-link);  
            text-decoration: none;  
            transition: color 150ms ease-in-out;  
        }  
        
        .project-link:hover {  
            color: var(--color-text-link-hover);  
            text-decoration: underline;  
        }  

        /* Cover Letter Section */  
        .cover-letter-card {  
             background-color: var(--color-bg-default);  
            border: 1px solid var(--color-border-default);  
            border-radius: var(--border-radius-medium);  
            padding: var(--space-8);  
            box-shadow: var(--shadow-small);  
        }  
        .cover-letter-card h3 {  
            font-size: 22px;  
            font-weight: 600;  
            margin-bottom: var(--space-2);  
        }  
        .cover-letter-card h4 {  
            font-size: 18px;  
            font-weight: 600;  
            margin-top: var(--space-6);  
            margin-bottom: var(--space-3);  
            padding-bottom: var(--space-2);  
            border-bottom: 1px solid var(--color-border-muted);  
        }  
        .cover-letter-card p {  
            font-size: 16px;  
            line-height: 1.7;  
            color: var(--color-text-secondary);  
            margin-bottom: var(--space-4);  
        }  

        /* Responsive Design */  
        @media (max-width: 996px) {  
            .main-content {  
                grid-template-columns: 1fr;  
                gap: var(--space-4);  
            }  

            .sidebar {  
                padding-right: 0;  
            }  

            .content-area {  
                padding-left: 0;  
            }  

            .avatar {  
                width: 80px;  
                height: 80px;  
                font-size: 26px;  
                margin-bottom: var(--space-2);  
            }  

            .avatar img {  
                width: 100%;  
                height: 100%;  
                object-fit: cover;  
                object-position: center 20%;  
            }  

            .profile-section {  
                display: flex;  
                align-items: center;  
                gap: var(--space-4);  
                margin-bottom: var(--space-6);  
            }  

            .profile-info {  
                flex: 1;  
            }  

            .nav-tabs {  
                overflow-x: auto;  
            }  

            .resume-grid {  
                grid-template-columns: 1fr;  
            }  
            
            .skills-card {  
                grid-column: 1;  
            }  

            .contribution-section {  
                overflow-x: auto;  
            }  
        }  

        @media (max-width: 480px) {  
            .container {  
                padding: 0 var(--space-3);  
            }  

            .profile-section {  
                flex-direction: column;  
                text-align: center;  
            }  

            .nav-tab {  
                margin-right: var(--space-4);  
            }  

            .project-card {  
                grid-template-columns: 1fr;  
            }  
        }  
    </style>
</head>
<body>
    <!-- Header -->
    <header class="header">
        <div class="container">
            <div class="header-content">
                <div class="logo">InHub</div>
            </div>
        </div>
    </header>

    <!-- Main Container -->
    <div class="container">
        <div class="main-content">
            <!-- Sidebar -->
            <aside class="sidebar">
                <div class="profile-section">
                    <div class="avatar"><img src="서인영 사진.jpg" alt="프로필 사진" onerror="this.onerror=null;this.src='https://placehold.co/296x296/EFEFEF/333333?text=Image+Not+Found';"/></div>
                    <div class="profile-info">
                        <h1 class="profile-name">서인영</h1>
                        <hr>
                        <div class="profile-stats">
                            <div class="stat-item">
                                <span class="stat-icon">🎂</span>
                                <span><strong>생년월일</strong></span>
                            </div>
                            <div class="stat-value">1999.12.29</div>
                            
                            <div class="stat-item">
                                <span class="stat-icon">✉️</span>
                                <span><strong>이메일</strong></span>
                            </div>
                            <div class="stat-value"><a href="mailto:dlsdud9098@naver.com" class="profile-link">dlsdud9098@naver.com</a></div>
                            
                            <div class="stat-item">
                                <span class="stat-icon">🐱</span>
                                <span><strong>깃허브</strong></span>
                            </div>
                            <div class="stat-value"><a href="https://github.com/dlsdud9098" target="_blank" class="profile-link">github.com/dlsdud9098</a></div>
                            
                            <div class="stat-item">
                                <span class="stat-icon">💾</span>
                                <span><strong>블로그</strong></span>
                            </div>
                            <div class="stat-value"><a href="https://velog.io/@dlsdud9098" target="_blank" class="profile-link">dlsdud9098/velog.io</a></div>
                        </div>

                        <!-- GitHub Contribution Chart -->
                        <div class="contribution-section" align="center">
                            <div class="contribution-title">
                                <span>🌿</span>
                                최근 3개월 잔디 현황  
                            </div>
                            <table class="contribution-calendar">
                                <thead>
                                    <tr>
                                        <td></td>
                                        <td class="contrib-month-label" colspan="4">May</td>
                                        <td class="contrib-month-label" colspan="5">Jun</td>
                                        <td class="contrib-month-label" colspan="4">Jul</td>
                                    </tr>
                                </thead>
                                <tbody>
                                    <!-- Sunday -->
                                    <tr>
                                        <td class="contrib-day-label">Sun</td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="0"></div></td>
                                        <td><div class="contrib-day" data-level="0"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="0"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                    </tr>
                                    <!-- Monday -->
                                    <tr>
                                        <td class="contrib-day-label">Mon</td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="2"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="0"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                    </tr>
                                    <!-- Tuesday -->
                                    <tr>
                                        <td class="contrib-day-label">Tue</td>
                                        <td><div class="contrib-day" data-level="0"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="0"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="2"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="2"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="2"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                    </tr>
                                    <!-- Wednesday -->
                                    <tr>
                                        <td class="contrib-day-label">Wed</td>
                                        <td><div class="contrib-day" data-level="2"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="0"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="0"></div></td>
                                        <td><div class="contrib-day" data-level="2"></div></td>
                                        <td><div class="contrib-day" data-level="2"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="2"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                    </tr>
                                    <!-- Thursday -->
                                    <tr>
                                        <td class="contrib-day-label">Thu</td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="0"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="2"></div></td>
                                    </tr>
                                    <!-- Friday -->
                                    <tr>
                                        <td class="contrib-day-label">Fri</td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="2"></div></td>
                                        <td><div class="contrib-day" data-level="0"></div></td>
                                        <td><div class="contrib-day" data-level="0"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="0"></div></td>
                                        <td><div class="contrib-day" data-level="2"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                    </tr>
                                    <!-- Saturday -->
                                    <tr>
                                        <td class="contrib-day-label">Sat</td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="0"></div></td>
                                        <td><div class="contrib-day" data-level="0"></div></td>
                                        <td><div class="contrib-day" data-level="0"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="0"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                        <td><div class="contrib-day" data-level="1"></div></td>
                                    </tr>
                                </tbody>
                            </table>
                            
                        </div>
                    </div>
                </div>
            </aside>

            <!-- Main Content Area -->
            <main class="content-area">
                <!-- Navigation -->
                <nav class="navigation">
                    <ul class="nav-tabs">
                        <li class="nav-tab active"><a href="#overview">개요</a></li>
                        <li class="nav-tab"><a href="#repositories">프로젝트</a></li>
                        <li class="nav-tab"><a href="#projects">자기소개서</a></li>
                    </ul>
                </nav>

                <!-- Resume Overview -->
                <section class="content-section">
                    <div class="resume-grid">
                        <!-- Education -->
                        <div class="resume-card">
                            <h2 class="card-title">🏫 학력</h2>
                            <div class="card-content">
                                <div class="item">
                                    <div class="item-title">건국대학교(충주) 졸업</div>
                                    <li>소프트웨어학과 (2018.03 ~ 2025.02)</li>
                                </div>
                                <div class="item">
                                    <div class="item-title">덕수고등학교 졸업</div>
                                    <li>컴퓨터과 (2015.03 ~ 2018.02)</li>
                                </div>
                            </div>
                            <br>
                            <h2 class="card-title">🎒 활동</h2>
                            <div class="card-content">
                                <div class="item">
                                    <div class="item-title">데이터 AI 개발자</div>
                                    <li>서울청년취업사관학교 (2025.05 ~ 진행중)</li>
                                    <li>Python, MySQL, Git</li>
                                </div>
                                <div class="item">
                                    <div class="item-title">세미콜론</div>
                                    <li>고등학교 교내 동아리</li>
                                    <li>Android, Java</li>
                                </div>
                            </div>
                        </div>

                        <!-- Certificates -->
                        <div class="resume-card">
                            <h2 class="card-title">🧾 자격증</h2>
                            <div class="card-content">
                                <div class="cert-group">
                                    <div class="cert-category">Docs:</div>
                                    <div>
                                        <li>Office Excel® 2010 (2018)</li>
                                        <li>Office PowerPoint® 2010 (2018)</li>
                                        <li>ITQ 아래한글 A등급 (2015)</li>
                                        <li>ITQ 한글파워포인트 B등급 (2015)</li>
                                        <li>IT PLUS LEVEL 4 (2017)</li>
                                    </div>
                                </div>
                                <div class="cert-group">
                                    <div class="cert-category">Develop:</div>
                                    <div>
                                        <li>정보처리기사 (필기) (2025)</li>
                                        <li>ADsP (2024)</li>
                                        <li>정보처리기능사 (2017)</li>
                                        <li>GTQ 2급 (2015)</li>
                                    </div>
                                </div>
                                <div class="cert-group">
                                    <div class="cert-category">etc:</div>
                                    <div>
                                        <li>2종 보통 (2020)</li>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Skills -->
                        <div class="resume-card skills-card">
                            <h2 class="card-title">⛏️ 스킬</h2>
                            <div class="card-content">
                                <table class="skills-table">
                                    <thead>
                                        <tr>
                                            <th>분류</th>
                                            <th>주요 스킬</th>
                                            <th>사용 경험</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td>🔤 Language</td>
                                            <td class="skill-primary">Python</td>
                                            <td>C/C++, JavaScript, Java, R, Swift</td>
                                        </tr>
                                        <tr>
                                            <td>⚙️ Backend</td>
                                            <td>-</td>
                                            <td>Flask, Django</td>
                                        </tr>
                                        <tr>
                                            <td>🎨 Frontend</td>
                                            <td>-</td>
                                            <td>React, Html5, CSS, Flutter, Astro</td>
                                        </tr>
                                        <tr>
                                            <td>🗄️ Database</td>
                                            <td class="skill-primary">MySQL</td>
                                            <td>MongoDB</td>
                                        </tr>
                                        <tr>
                                            <td>🔧 DevOps</td>
                                            <td class="skill-primary">Git, GitHub, Ubuntu</td>
                                            <td>Orange, Docker</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- Projects Section -->
                <section class="content-section">
                    <h2 class="card-title" style="font-size: 20px; margin-bottom: var(--space-4);">🚀 프로젝트</h2>
                    <div class="project-list">
                        <!-- Project 1 -->
                        <div class="project-card">
                            <div class="project-image">
                                <img src="https://placehold.co/150x150/E2E8F0/4A5568?text=Project+1" alt="웹툰, 소설 추천 사이트">
                            </div>
                            <div class="project-details">
                                <h3>웹툰, 소설 추천 사이트</h3>
                                <p><strong>개요:</strong> 사용자 취향을 분석하여 웹툰과 소설을 추천하는 플랫폼입니다.</p>
                                <p><strong>개발 인원:</strong> 4명</p>
                                <p><strong>개발 일자:</strong> 2024.03 - 2024.05</p>
                                <div class="project-links">
                                    <a href="#" class="project-link">자세히 보기</a>
                                    <a href="#" class="project-link">깃허브 보기</a>
                                </div>
                            </div>
                        </div>
                        <!-- Project 2 -->
                        <div class="project-card">
                            <div class="project-image">
                                <img src="https://placehold.co/150x150/CBD5E0/4A5568?text=Project+2" alt="가상 염색 시뮬레이터">
                            </div>
                            <div class="project-details">
                                <h3>가상 염색 시뮬레이터</h3>
                                <p><strong>개요:</strong> AI를 활용하여 사용자 사진에 다양한 헤어 컬러를 적용해보는 시뮬레이터입니다.</p>
                                <p><strong>개발 인원:</strong> 1명 (개인 프로젝트)</p>
                                <p><strong>개발 일자:</strong> 2024.01 - 2024.02</p>
                                <div class="project-links">
                                    <a href="#" class="project-link">자세히 보기</a>
                                    <a href="#" class="project-link">깃허브 보기</a>
                                </div>
                            </div>
                        </div>
                         <!-- Project 3 -->
                        <div class="project-card">
                            <div class="project-image">
                                <img src="https://placehold.co/150x150/BEE3F8/2D3748?text=Project+3" alt="영상 질감 바꾸기">
                            </div>
                            <div class="project-details">
                                <h3>영상 질감 바꾸기</h3>
                                <p><strong>개요:</strong> 영상에 유화, 수채화 등 예술적인 질감을 적용하는 프로그램입니다.</p>
                                <p><strong>개발 인원:</strong> 1명 (개인 프로젝트)</p>
                                <p><strong>개발 일자:</strong> 2023.11 - 2023.12</p>
                                <div class="project-links">
                                    <a href="#" class="project-link">자세히 보기</a>
                                    <a href="#" class="project-link">깃허브 보기</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
                
                <!-- Cover Letter Section -->
                <section class="content-section">
                    <h2 class="card-title" style="font-size: 20px; margin-bottom: var(--space-4);">📝 자기소개서</h2>
                    <div class="cover-letter-card">                        
                        <h3>기술로 더 안전한 세상을 만드는 TISC의 비전에 동참하고 싶습니다.</h3>
                        <hr>
                        <p>대학교 3학년, ChatGPT를 통해 AI가 인간의 삶을 혁신할 무한한 잠재력을 목격하며 AI/ML 엔지니어의 꿈을 키웠습니다. 기술 자체에 대한 호기심을 넘어, AI 기술로 실제 세상의 문제를 해결하고 가치를 창출하는 개발자가 되겠다는 명확한 목표를 세웠습니다. 이러한 저의 비전은 3D LiDAR와 카메라의 센서 퓨전 기술을 통해 스마트시티와 산업 현장의 안전을 책임지는 (주)티아이에스씨(TISC)의 방향성과 정확히 일치합니다.</p>
                        <p>특히 악천후 속에서도 객체 인식의 신뢰성을 획기적으로 높인 'LiCas' 솔루션과, 교통 데이터를 분석하여 보행자의 안전을 지키는 'MaRu' 솔루션에 깊은 감명을 받았습니다. 이는 제가 이미지, 음성, 텍스트 등 다양한 데이터를 다루는 멀티모달 AI 프로젝트들을 진행하며 추구해온 '다양한 정보의 융합을 통한 문제 해결'이라는 가치와 맞닿아 있습니다. TISC의 독보적인 엣지 AI 기술력에 저의 성장 잠재력을 더하여, 기술로 더 안전하고 효율적인 사회를 만드는 여정에 함께하고 싶어 지원하게 되었습니다.</p>
                        <br>
                        <h3>문제의 본질을 파고드는 집요함과 시스템 최적화 경험</h3>
                        <hr>
                        <p>저는 주어진 과제를 해결하는 것을 넘어, 문제의 본질을 파고들어 더 나은 결과를 만드는 과정을 즐깁니다. 두 가지 핵심 프로젝트 경험을 통해 저의 문제 해결 능력과 시스템 최적화 역량을 증명하고 싶습니다.</p>
                        <p><strong>첫째, 포기하지 않는 집요함으로 영상의 완성도를 높인 경험이 있습니다.</strong><br>Stable Diffusion을 활용해 동영상을 변환하는 프로젝트에서, 인물의 표정이 어색하게 변하는 문제에 직면했습니다. 프로젝트 기한과 이미 확보된 결과물을 고려하면 타협할 수도 있었지만, 더 높은 완성도를 위해 문제 해결에 매달렸습니다. 먼저 'EbSynth'라는 도구를 적용해 보았으나, 눈을 감았다 뜨는 장면에서 여전히 한계가 있었습니다. 이에 안주하지 않고, 영상의 모든 프레임을 분석해 '눈 크기'를 기준으로 눈을 뜨고 있는 프레임을 자동 선별하고, 이를 눈 감은 구간에 '추가 키프레임'으로 삽입하는 로직을 직접 구현했습니다. 그 결과, 인물의 눈 깜빡임과 표정 변화가 훨씬 자연스러워진 결과물을 얻을 수 있었습니다. 이 경험을 통해 문제의 본질을 파고들어 해결책을 찾아낼 때 비로소 기술적 성장을 이룰 수 있다는 것을 배웠습니다.</p>
                        <p><strong>둘째, 점진적 개선을 통해 데이터 수집 성능을 2배 향상시킨 경험이 있습니다.</strong><br>대규모 데이터 수집 프로젝트 초기, Selenium 기반의 동적 크롤러는 5시간 이상의 실행 시간이 소요되었습니다. 저는 이 비효율을 개선하기 위해 첫 단계로 Playwright를 도입하여 실행 시간을 2~3시간으로 단축했습니다. 여기서 멈추지 않고, 브라우저의 cURL 요청을 분석하여 UI 렌더링 과정을 생략하고 API를 직접 호출하는 방식으로 변경했습니다. 이 접근법을 통해 최종 실행 시간을 1~2시간으로 단축하며 약 2배 이상의 성능 개선을 이뤄냈습니다. 이 과정은 제한된 자원 내에서 최고의 효율을 추구해야 하는 엣지 컴퓨팅 환경에 대한 저의 높은 이해도와 시스템 최적화 역량을 보여주는 경험이라고 생각합니다.</p>
                        <p>이 외에도 이미지 분류, AI 가수, 소설 장르 예측 등 다양한 미니 프로젝트를 통해 이미지, 음성, 텍스트 데이터를 다루는 멀티모달 AI에 대한 폭넓은 시야와 실무 경험을 갖추었습니다.</p>
                        <br>
                        <h3>이론적 갈증을 성장의 동력으로 삼는 개발자</h3>
                        <hr>
                        <p>저는 혼자서 프로젝트를 진행하며 아이디어를 빠르게 구현하는 능력을 길렀지만, 이 과정에서 '왜 이 코드를 사용해야 하는가'에 대한 이론적 깊이의 부족함을 절감했습니다. 단순히 기능을 구현하는 것을 넘어, 기술의 근본 원리를 이해하고 싶다는 갈증은 저를 청년취업사관학교 인공지능 부트캠프로 이끌었습니다.</p>
                        <p>부트캠프에서 컴퓨터 비전, 딥러닝의 이론적 토대를 견고히 다지고, 다양한 팀 프로젝트를 통해 동료와 협업하며 시너지를 창출하는 방법을 배우고 있습니다. 특히, 저의 부족함을 솔직하게 인정하고 이를 해결하기 위해 주도적으로 학습 환경에 뛰어든 경험은, 저의 가장 큰 강점인 '지속적인 학습을 수용하는 적응력'과 '성장 잠재력'을 보여준다고 생각합니다. TISC의 일원으로서 3D 포인트 클라우드 처리, 센서 퓨전과 같은 새로운 기술 분야에 직면했을 때, 두려움 없이 학습하고 빠르게 적응하여 팀에 기여할 수 있다고 자신합니다.</p>
                        <br>
                        <h3>TISC의 엣지 AI 솔루션에 기여하고 함께 성장하겠습니다.</h3>
                        <hr>
                        <p>TISC에 입사하게 된다면, 저의 시스템 최적화 경험과 문제 해결 능력을 바탕으로 회사의 기술 발전에 기여하고 싶습니다.</p>
                        <p>단기적으로는 TISC의 3D 포인트 클라우드 처리 파이프라인과 데이터셋을 빠르게 학습하고, 저의 모델 경량화 및 최적화 경험을 살려 '7EYE'와 'LiCas' 솔루션의 엣지 디바이스 연산 효율을 개선하는 데 기여하겠습니다.</p>
                        <p>장기적으로는 스마트시티 환경에서 수집된 시계열 데이터를 바탕으로 보행자의 동선과 행동을 예측하는 모델을 개발하여, 'MaRu' 솔루션이 단순한 사후 관제를 넘어 사고를 미연에 방지하는 '예측 AI 시스템'으로 발전하는 데 핵심적인 역할을 수행하고 싶습니다.</p>
                        <p>대표님의 메시지에서 "발전의 길은 절대 일직선이 아니다"라는 문구를 인상 깊게 보았습니다. 저 또한 수많은 기술적 난관과 실패를 성장의 발판으로 삼아왔습니다. TISC에서 끊임없이 도전하고 동료들과 함께 장애물을 극복하며, '3D 인지 기술을 통한 스마트 사회 구축'이라는 비전을 함께 실현해나가는 개발자가 되겠습니다.</p>
                    </div>
                </section>
            </main>
        </div>
    </div>

    <script>
        // Tab navigation functionality  
        function initializeNavigation() {  
            const tabs = document.querySelectorAll('.nav-tab a');  
            tabs.forEach(tab => {  
                tab.addEventListener('click', (e) => {  
                    e.preventDefault();  
                    
                    // Remove active class from all tabs  
                    document.querySelectorAll('.nav-tab').forEach(t => t.classList.remove('active'));  
                    
                    // Add active class to clicked tab  
                    tab.closest('.nav-tab').classList.add('active');  
                });  
            });  
        }  

        // Initialize functionality  
        document.addEventListener('DOMContentLoaded', () => {  
            initializeNavigation();  
        });  
    </script>
</body>
</html>