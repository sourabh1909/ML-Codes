import streamlit as st
from dbhelper import DB
import plotly.graph_objects as go
import pandas as pd

db = DB()

st.set_page_config(
    page_title="Flight Analytics Dashboard",
    page_icon="✈️",
    layout="wide",   # or "centered"
    initial_sidebar_state="expanded"
)

def home_page():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        /* ── Hero ── */
        .hero-wrapper {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 60%, #0f2a1e 100%);
            border-radius: 20px;
            padding: 52px 48px 44px;
            margin-bottom: 36px;
            border: 1px solid #1e3a2e;
            position: relative;
            overflow: hidden;
        }
        .hero-wrapper::before {
            content: "";
            position: absolute;
            top: -60px; right: -60px;
            width: 260px; height: 260px;
            background: radial-gradient(circle, rgba(0,201,167,0.12) 0%, transparent 70%);
            border-radius: 50%;
            pointer-events: none;
        }
        .hero-tag {
            display: inline-block;
            background: rgba(0,201,167,0.12);
            color: #00C9A7;
            border: 1px solid rgba(0,201,167,0.3);
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            padding: 4px 14px;
            margin-bottom: 18px;
        }
        .hero-title {
            font-size: 42px;
            font-weight: 700;
            color: #f8fafc;
            margin: 0 0 12px;
            line-height: 1.15;
        }
        .hero-title span {
            color: #00C9A7;
        }
        .hero-sub {
            font-size: 16px;
            color: #94a3b8;
            max-width: 560px;
            line-height: 1.7;
            margin: 0;
        }

        /* Section heading*/
        .section-heading {
            font-size: 11px;
            font-weight: 600;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            color: #64748b;
            margin: 0 0 16px;
        }

        /* tag badges */
        .badge-row {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 32px;
        }
        .badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 8px 16px;
            border-radius: 10px;
            font-size: 13px;
            font-weight: 500;
        }
        .badge-teal  { background:#0f2a24; color:#34d399; border:1px solid #14532d; }
        .badge-blue  { background:#0f1e35; color:#60a5fa; border:1px solid #1e3a5f; }
        .badge-violet{ background:#1a1030; color:#a78bfa; border:1px solid #2e1065; }
        .badge-amber { background:#2a1a00; color:#fbbf24; border:1px solid #451a03; }
        .badge-rose  { background:#2a0f1a; color:#fb7185; border:1px solid #4c0519; }
        .badge-dot {
            width: 7px; height: 7px;
            border-radius: 50%;
            display: inline-block;
        }
        .dot-teal   { background:#34d399; }
        .dot-blue   { background:#60a5fa; }
        .dot-violet { background:#a78bfa; }
        .dot-amber  { background:#fbbf24; }
        .dot-rose   { background:#fb7185; }

        /*cards*/
        .feature-card {
            background: #0f172a;
            border: 1px solid #1e293b;
            border-radius: 16px;
            padding: 24px;
            height: 100%;
            transition: border-color 0.2s;
        }
        .feature-card:hover { border-color: #334155; }
        .fc-icon {
            width: 42px; height: 42px;
            border-radius: 10px;
            display: flex; align-items: center; justify-content: center;
            font-size: 20px;
            margin-bottom: 14px;
        }
        .fc-icon-teal   { background: rgba(52,211,153,0.1); }
        .fc-icon-blue   { background: rgba(96,165,250,0.1); }
        .fc-icon-violet { background: rgba(167,139,250,0.1); }
        .fc-icon-amber  { background: rgba(251,191,36,0.1);  }
        .fc-title {
            font-size: 15px; font-weight: 600; color: #e2e8f0;
            margin: 0 0 6px;
        }
        .fc-desc {
            font-size: 13px; color: #64748b; line-height: 1.6; margin: 0;
        }

        /* ── Info trio cards ── */
        .info-card {
            background: #0f172a;
            border: 1px solid #1e293b;
            border-radius: 16px;
            padding: 20px 22px;
        }
        .info-card-label {
            font-size: 11px;
            font-weight: 600;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            color: #475569;
            margin: 0 0 12px;
        }
        .info-item {
            display: flex; align-items: center; gap: 10px;
            padding: 7px 0;
            border-bottom: 1px solid #1e293b;
            font-size: 13px; color: #cbd5e1;
        }
        .info-item:last-child { border-bottom: none; }
        .info-dot {
            width: 6px; height: 6px; border-radius: 50%;
            flex-shrink: 0;
        }

        /* ── Bottom cards ── */
        .bottom-card {
            background: #0f172a;
            border: 1px solid #1e293b;
            border-radius: 16px;
            padding: 22px 24px;
        }
        .bottom-card-title {
            font-size: 14px; font-weight: 600; color: #e2e8f0;
            margin: 0 0 14px;
        }
        .bottom-item {
            display: flex; align-items: flex-start; gap: 10px;
            font-size: 13px; color: #94a3b8;
            padding: 5px 0;
            line-height: 1.5;
        }
        .bottom-item-dot {
            width: 5px; height: 5px; border-radius: 50%;
            flex-shrink: 0; margin-top: 7px;
        }

        /* ── Footer ── */
        .footer {
            text-align: center;
            padding: 24px 0 8px;
            font-size: 13px;
            color: #475569;
        }
        .footer span { color: #00C9A7; font-weight: 600; }
        </style>
    """, unsafe_allow_html=True)

    # Hero
    st.markdown("""
        <div class="hero-wrapper">
            <div class="hero-tag">✈ Flight Analytics</div>
            <h1 class="hero-title">Explore. Analyze.<br><span>Fly Smarter.</span></h1>
            <p class="hero-sub">
                A real-time flight analytics platform powered by Streamlit and MySQL.
                Discover airline trends, busy routes, and daily traffic patterns — all in one place.
            </p>
        </div>
    """, unsafe_allow_html=True)


    st.markdown('<p class="section-heading">Built with</p>', unsafe_allow_html=True)
    st.markdown("""
        <div class="badge-row">
            <div class="badge badge-teal">  <span class="badge-dot dot-teal"></span>  Python      </div>
            <div class="badge badge-blue">  <span class="badge-dot dot-blue"></span>  Streamlit   </div>
            <div class="badge badge-violet"><span class="badge-dot dot-violet"></span> MySQL      </div>
            <div class="badge badge-amber"> <span class="badge-dot dot-amber"></span> Plotly      </div>
            <div class="badge badge-rose">  <span class="badge-dot dot-rose"></span>  Pandas      </div>
        </div>
    """, unsafe_allow_html=True)


    st.markdown('<p class="section-heading">Key features</p>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    features = [
        ("teal",   "🔍", "Flight Search",        "Search by source & destination with live DB queries."),
        ("blue",   "📊", "Airline Distribution",  "Interactive donut chart showing airline market share."),
        ("violet", "🏙️", "Busiest Airports",      "Rank cities by total flight traffic volume."),
        ("amber",  "📅", "Daily Trends",          "Visualize departure and arrival patterns over time."),
    ]
    for col, (color, icon, title, desc) in zip([c1, c2, c3, c4], features):
        with col:
            st.markdown(f"""
                <div class="feature-card">
                    <div class="fc-icon fc-icon-{color}">{icon}</div>
                    <p class="fc-title">{title}</p>
                    <p class="fc-desc">{desc}</p>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    i1, i2, i3 = st.columns(3)
    info_data = [
        ("Tech stack",  "#34d399", ["Python 3.x", "Streamlit", "MySQL"]),
        ("Libraries",   "#60a5fa", ["Pandas", "Plotly", "mysql-connector-python"]),
        ("Capabilities",  "#a78bfa", ["Search Flights", "Analytics", "Visualizations"]),
    ]
    for col, (label, dot_color, items) in zip([i1, i2, i3], info_data):
        with col:
            items_html = "".join(
                f'<div class="info-item"><span class="info-dot" style="background:{dot_color}"></span>{item}</div>'
                for item in items
            )
            st.markdown(f"""
                <div class="info-card">
                    <p class="info-card-label">{label}</p>
                    {items_html}
                </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)


    b1, b2 = st.columns(2)
    with b1:
        st.markdown("""
            <div class="bottom-card">
                <p class="bottom-card-title">Key learnings</p>
                <div class="bottom-item"><span class="bottom-item-dot" style="background:#34d399;"></span>Frontend + Backend Integration with Streamlit</div>
                <div class="bottom-item"><span class="bottom-item-dot" style="background:#34d399;"></span>SQL query optimization for real-time results</div>
                <div class="bottom-item"><span class="bottom-item-dot" style="background:#34d399;"></span>Data visualization with Plotly charts</div>
            </div>
        """, unsafe_allow_html=True)
    with b2:
        st.markdown("""
            <div class="bottom-card">
                <p class="bottom-card-title">Future scope</p>
                <div class="bottom-item"><span class="bottom-item-dot" style="background:#a78bfa;"></span>ML-based price prediction model</div>
                <div class="bottom-item"><span class="bottom-item-dot" style="background:#a78bfa;"></span>Interactive map-based route visualization</div>
                <div class="bottom-item"><span class="bottom-item-dot" style="background:#a78bfa;"></span>Cloud deployment on Streamlit Cloud / AWS</div>
            </div>
        """, unsafe_allow_html=True)

    # footer
    st.markdown("""
        <div class="footer">
            Built with <span>Streamlit</span> &nbsp;·&nbsp; Powered by MySQL &nbsp;·&nbsp; Visualized with Plotly
        </div>
    """, unsafe_allow_html=True)




st.sidebar.title('Flights Analytics')

user_option = st.sidebar.selectbox('Menu',['Select One','Check Flights','Analytics'])

if user_option == 'Check Flights':
    
    st.title('Check Flights')
    
    col1,col2 = st.columns(2)
    city = db.fetch_city_names()
    
    with col1:
        source = st.selectbox('Source',sorted(city))
    
    with col2:
        destination = st.selectbox('Destination',sorted(city))
        
    if st.button('Search'):
        result=db.fetch_all_flights(source,destination)
        
        if result:
            df = pd.DataFrame(result, columns=[
                "Airline", "Route", "Time", "Duration (min)", "Price (₹)"
            ])
            st.dataframe(df)
        else:
            st.warning("No filght found between this route")
            
elif user_option == 'Analytics':

    # PIE CHART
    airline, freq = db.fetch_airline_ferq()

    fig = go.Figure(
        go.Pie(
            labels=airline,
            values=freq,
            hole=0.4,
            textinfo='percent',
            textfont=dict(size=16),
            insidetextorientation='radial'
        )
    )

    fig.update_layout(template='plotly_dark')

    st.header("Airline Distribution")
    st.plotly_chart(fig, width='stretch')


    # BAR CHART
    city, freq2 = db.busy_airport()

    fig = go.Figure(
        go.Bar(
            x=city,
            y=freq2,
            marker=dict(color=freq2, colorscale='viridis')
        )
    )

    fig.update_layout(template='plotly_dark')

    st.header("Busiest Airports")
    st.plotly_chart(fig, width='stretch')


    # LINE CHART
    date, freq1 = db.daily_freq()

    fig = go.Figure(
        go.Scatter(
            x=date,
            y=freq1,
            mode='lines+markers',
            line=dict(color='cyan')
        )
    )

    fig.update_layout(template='plotly_dark')

    st.header("Daily Flight Trend")
    st.plotly_chart(fig,width='stretch')

    data = db.flights_analysis()
    print(data)
    
else:
    home_page()
    

