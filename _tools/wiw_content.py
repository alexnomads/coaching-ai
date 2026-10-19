# Content for /who-i-work-with/ (the client city).
# Every persona is anonymised: no names, no cities, country (or continent) only.
# "status" is honest: "Result" only where a real outcome exists.

DISTRICTS = [
    {"id": "old-town", "name": "Old Town", "tag": "Owners & operators",
     "blurb": "Service businesses where every job is a new quote, a new site or a new order. AI here has to survive real operations."},
    {"id": "business-district", "name": "Business District", "tag": "Leaders & regulated work",
     "blurb": "People whose decisions carry weight: a CEO, a clinic, an auditor, a safety-critical project. AI here has to be checkable."},
    {"id": "market-square", "name": "Market Square", "tag": "Marketing & sales",
     "blurb": "People who live on attention and pipeline. AI here has to sound human and bring in work."},
    {"id": "the-station", "name": "The Station", "tag": "Changing track",
     "blurb": "For people moving to their next role. AI here builds the case for where you go next."},
]

P = []

P.append(dict(
    num="01", slug="events-production-companies", district="old-town", building="stage",
    persona="The Operations-Heavy <em>Owner</em>", persona_plain="The Operations-Heavy Owner",
    sector="Events & live production", country="Italy", status="Result",
    h1="AI for event and live production companies",
    title="AI for Event Production Companies: Quotes & Briefs on Autopilot",
    desc="How an event production company automated 85–90% of its quotes and team briefs with AI. A day in the life, what was built, and how to start.",
    roles=["Owner", "Ops lead", "Team coordinator"],
    answer="An event production company can use AI to turn one site-visit transcript into three documents at once: a logistics brief, a technical brief and a client quote. The trick is a written price list and discount rules the AI can read, not a longer prompt.",
    story=[
        "You run a service business where every job means a new quote, a new brief and a new set of moving pieces: technical specs for your crew, a polished version for the client. You tried handing this to AI and it broke on anything past a simple request: wrong layout, missing line items, output the team couldn't use.",
        "<strong>The problem was never the tool. It was treating a 400-events-a-year business like a single prompt.</strong> Once the work was split into the right documents for the right people, with a real price list and written discount rules behind it, the result looked completely different.",
    ],
    result="Quote and briefing work now runs at roughly 85–90% automated. The owner steps in for strategy and genuine edge cases.",
    day=[
        ("08:00", "Voice notes from yesterday's site visit sit in your phone.", "The transcript goes into the project. Three drafts are waiting before coffee."),
        ("10:00", "You rewrite the same job twice: once for the crew, once for the client.", "Logistics and technical briefs go to the team in their own format."),
        ("13:00", "Pricing depends on who's asking. It lives in your head.", "Discount rules by client type are written down. The AI applies them and asks when unsure."),
        ("16:00", "The quote goes out late, with a line item missing.", "The quote follows your real template and price list. You check, not type."),
        ("19:00", "You're still on email.", "You're on site, where the business actually happens."),
    ],
    signals=[
        "I've tried AI for quotes and proposals but it falls apart on anything complex",
        "My team needs different information than my clients do, and I'm rewriting the same job twice",
        "I don't have time to become a prompt engineer. I need this to just work",
        "Nothing is written down anywhere AI could use",
    ],
    outcomes=[
        "A split-document system: one output for internal ops, one for the client",
        "A written brief for each role on your team, so AI stops guessing what done looks like",
        "A realistic automation percentage for your business, not a vague promise",
        "A prioritised list of what to hand off first and what to keep",
    ],
    tools=["Claude Projects", "Google Drive", "Price list as CSV", "Voice notes"],
    faq=[
        ("Can AI write quotes for an event production company?", "Yes, if it has your real price list, your discount rules and two or three example quotes to copy. Without those it guesses, and guesses are what break on complex jobs."),
        ("Do I need to change software?", "No. The setup in this engagement used the owner's existing Google Drive and a Claude Project. The new part was writing down rules that only existed in his head."),
        ("How long before it saves time?", "The first real-transcript test produced a usable brief and quote within the first few lessons. Most of the work after that is filling gaps the AI exposes, like a missing artist price list."),
    ],
))

P.append(dict(
    num="02", slug="engineering-infrastructure", district="business-district", building="crane",
    persona="The Regulated-Industry <em>Specialist</em>", persona_plain="The Regulated-Industry Specialist",
    sector="Permits & compliance on infrastructure projects", country="International projects", status="Result",
    h1="AI for engineering and infrastructure compliance work",
    title="AI for Engineering & Infrastructure: Verifiable Systems, Not Chatbots",
    desc="How a permit-to-work coordinator on international infrastructure projects built verifiable AI sub-systems with zero data loss between sites.",
    roles=["Compliance", "Technical lead", "Auditor"],
    answer="In regulated engineering work, AI is useful when it is built as small, checkable agents with defined inputs and rules, not as one chat window. Each agent does one job, and a human can verify every hand-off.",
    story=[
        "You work where getting it wrong has real consequences: safety documentation, permits, coordination across several sites, all under scrutiny. You don't want a chatbot. You want a system you can verify.",
        "<strong>This isn't about typing better prompts. It's about building a multi-step system</strong>: agents that handle defined pieces of the work, with rules you can check and no silent data loss between steps.",
    ],
    result="Verified sub-systems with zero data loss between sites, now scaling toward a full coordinating system. The client has since expanded the project on their own initiative.",
    day=[
        ("07:30", "Permits from three sites arrive in three formats.", "One intake agent normalises them into a single checked format."),
        ("09:00", "You cross-check documents by hand against the rules.", "A rules agent flags what's missing. You review the flags, not every page."),
        ("12:00", "Two sites, two time zones, one spreadsheet that drifts.", "Each hand-off is logged. Nothing changes between sites without a record."),
        ("15:00", "An auditor asks why a permit was approved.", "The trail is there: input, rule applied, who signed."),
        ("18:00", "You stay late to make sure nothing slipped.", "You go home knowing what the system did and why."),
    ],
    signals=[
        "I need something more rigorous than a chat window I can't fully trust",
        "Coordination across sites eats hours every week",
        "I don't just want output. I want to verify it's correct",
        "Most AI-for-business advice is too generic for high-stakes work",
    ],
    outcomes=[
        "A map of which steps can be automated safely and which need a human check",
        "A working, verifiable first system, not a demo",
        "A framework to scale from one working piece to a coordinated system",
        "Confidence in exactly what the system is doing at every step",
    ],
    tools=["Claude Code", "Self-hosted agents (VPS)", "Structured logs"],
    faq=[
        ("Is AI safe for permit-to-work and compliance documents?", "It can be, when every agent has narrow rules and every output is checked by a person before it counts. The AI drafts and flags; the qualified person approves."),
        ("Should regulated teams use self-hosted AI?", "Often yes, for data control. Agents on your own server keep documents out of consumer chat apps and give you a full log of what ran."),
        ("Where do you start?", "With one sub-system that has a clear input and a clear check, such as normalising permits from different sites. Prove it, then connect the next one."),
    ],
))

P.append(dict(
    num="03", slug="in-house-marketing-teams", district="market-square", building="studio",
    persona="The In-House Marketing <em>Lead</em>", persona_plain="The In-House Marketing Lead",
    sector="Corporate marketing & creative production", country="Italy", status="Result",
    h1="AI video production for in-house marketing teams",
    title="AI Video for In-House Marketing Teams: A Real Production Pipeline",
    desc="How an in-house marketing lead built a consistent AI video pipeline for a company campaign: character and location sheets, cinematography spec, live deliverable.",
    roles=["Creative director", "Content lead", "Campaign manager"],
    answer="AI video looks professional when you lock characters and locations before generating anything, then follow a written cinematography plan. Consistency sheets and a shot spec matter more than which video tool you pick.",
    story=[
        "You own marketing output for your company, and that now means video. You tried AI video tools and hit the problem fast: characters and locations drift between shots, and nothing looks good enough to carry the brand.",
        "<strong>The fix isn't a better tool. It's the discipline real production uses</strong>: lock character and location consistency first, then shoot from a cinematography plan instead of one-off prompts.",
    ],
    result="Full production pipeline built: consistency system, cinematography spec and a live deliverable used in a company campaign at a major industry event.",
    day=[
        ("09:00", "The brief says 'a short video for the event'. No crew, no budget.", "You write the script with AI, then break it into shots."),
        ("10:30", "Every clip shows a slightly different person.", "Character and location sheets lock how everyone and everything looks."),
        ("13:00", "You try five video tools and get five styles.", "A written shot spec goes into the tool that fits each shot."),
        ("16:00", "Stitching clips together looks amateur.", "Camera moves and lighting are planned, so the edit holds together."),
        ("18:00", "You wonder if it's good enough to show the CEO.", "It goes into the real campaign."),
    ],
    signals=[
        "I can generate clips, but stitching them into something coherent is a mess",
        "My characters and settings look different in every shot",
        "I need something polished enough for a real campaign",
        "I don't have a production background. I need a system I can follow",
    ],
    outcomes=[
        "A reusable consistency system for characters and locations",
        "A written cinematography spec you can hand to any AI video tool",
        "A comparison of the current AI video tools, so you stop guessing",
        "A real campaign asset, not just techniques",
    ],
    tools=["Kling", "Seedance", "Venice AI", "CapCut", "Claude"],
    faq=[
        ("How do you keep characters consistent in AI video?", "Make a character reference sheet first: turnaround, close-ups, expressions, palette and a 'do not change' list. Use its panels as image references in every shot prompt."),
        ("Which AI video tool is best for marketing?", "It changes every few months. Pick per shot: some tools handle people better, others camera movement. The written shot spec is what keeps the result consistent across tools."),
        ("Can a marketing lead do this without a film background?", "Yes. This engagement started with no production background. The method borrows the steps real productions use and turns them into checklists."),
    ],
))

P.append(dict(
    num="04", slug="freelance-consultants", district="market-square", building="cottage",
    persona="The Multi-Client <em>Freelancer</em>", persona_plain="The Multi-Client Freelancer",
    sector="Freelance services", country="Switzerland & beyond", status="Result",
    h1="AI for freelancers who serve several clients",
    title="AI for Freelancers With Multiple Clients: Reporting & Admin Systems",
    desc="How multi-client freelancers use AI to stop rebuilding the same reports and admin by hand: a live reporting system, invoicing and client lists.",
    roles=["Consultant", "Freelancer", "Virtual assistant"],
    answer="A freelancer with several clients gets the most from AI by building one reusable system around the work they repeat every month, such as client reports, invoices and client lists, connected to real data instead of copy-paste.",
    story=[
        "You serve several clients at once, and a big part of your week goes on work that grows nobody's business: the same recap deck rebuilt by hand, invoices, client lists. You know AI should handle this. You haven't had time to build it properly.",
        "<strong>The unlock isn't a generic AI tool. It's a system built around your actual workflow</strong>, connected to real data, reused across every client instead of starting from scratch each month.",
    ],
    result="One freelancer went from a hand-built monthly deck to an interactive reporting system on live data, and won a new client partly because of it. A second, in Switzerland, is turning a self-built invoicing tool for a freelance fitness business into cooperating agents.",
    day=[
        ("08:30", "Monday: five clients want five reports.", "Reports refresh from live data. You add the commentary only you can write."),
        ("11:00", "Invoices are made one by one from a template.", "Invoices and client lists come from one place, built with AI, no subscription."),
        ("14:00", "A prospect asks what reporting looks like.", "You show them the live system. It sells for you."),
        ("16:00", "Admin eats the hours you could bill.", "Small agents handle the repeat work and hand each other the next step."),
        ("18:00", "More clients would mean more evenings.", "More clients means more rows in the same system."),
    ],
    signals=[
        "I rebuild the same report every month for different clients",
        "I know AI could speed this up, but I don't have a structured way to build it",
        "Clients expect faster, sharper reporting than I can deliver by hand",
        "I want more clients, not more hours",
    ],
    outcomes=[
        "A reusable reporting system built around how you work",
        "A path to connect real client data instead of copy-paste",
        "Deliverables clients notice, which help win the next one",
        "Hours back each month for billable work",
    ],
    tools=["Claude", "Interactive HTML dashboards", "Google Sheets", "Self-built tools"],
    faq=[
        ("How can freelancers automate client reporting with AI?", "Pick the one report you rebuild most often, connect it to the data source, and have AI generate the structure and charts. Keep the two or three lines of real insight for yourself."),
        ("Can I replace paid software with something I build with AI?", "Often, for simple tools like invoicing or client lists. Check what you lose first: backups, tax rules and support still matter."),
        ("What are cooperating agents?", "Small AI helpers that each do one job, like booking, invoicing or reminders, and pass the result to the next one. Easier to fix than one big assistant."),
    ],
))

P.append(dict(
    num="05", slug="sales-professionals", district="market-square", building="kiosk",
    persona="The Sales Pro Wanting an <em>Edge</em>", persona_plain="The Sales Pro Wanting an Edge",
    sector="Sales & business development", country="Europe", status="Target",
    h1="AI for sales professionals and business developers",
    title="AI for Sales Professionals: Prospecting & Research Without Sounding Like a Bot",
    desc="An AI workflow for account executives, BDRs and consultants: smarter prospecting, personalised outreach and pre-call research in minutes.",
    roles=["Account executive", "BDR", "Consultant"],
    answer="Salespeople get the most from AI in research and preparation: account research, call prep and first drafts of outreach. The human part stays the relationship and the judgement about what to say.",
    story=[
        "You're good at what you do. But the top performers around you use AI to prospect smarter, personalise faster and research deeper, and the gap widens every quarter.",
        "<strong>You have the instinct and the relationships. You need the right tools on top of them.</strong> Not generic prompts: a workflow built around how you actually sell.",
    ],
    result="Goal set in the engagement: cut pre-call research from 45 minutes to 5.",
    day=[
        ("08:00", "You scroll LinkedIn looking for who to call.", "A short list of accounts with a reason to call today is ready."),
        ("09:30", "Each email starts from a blank page.", "First drafts use real details from the account. You make them yours."),
        ("12:00", "45 minutes of prep before a call.", "Five minutes with a one-page brief: company, person, likely objections."),
        ("15:00", "Notes stay in your head after the call.", "The call summary and next steps write themselves into your CRM."),
        ("17:30", "You wonder how the top rep does it.", "Now you know."),
    ],
    signals=[
        "I want to use AI for outreach without sounding like a bot",
        "I need to look AI-fluent to clients and management",
        "The best reps are closing more. I want to know exactly how",
        "My research and prep take too long",
    ],
    outcomes=[
        "An AI prospecting workflow tailored to your sales motion",
        "Prompt frameworks for outreach that doesn't read as generated",
        "A pre-call research system: 5 minutes instead of 45",
        "A way to position your AI fluency with clients",
    ],
    tools=["Claude", "LinkedIn", "Your CRM", "Call recorders"],
    faq=[
        ("How do salespeople use AI without sounding robotic?", "Use AI for research and structure, then write the opening line and the ask yourself. Specific details about the person beat any template."),
        ("What's the fastest AI win in sales?", "Pre-call research. A one-page brief on the company and person, built from public sources, saves the most time in the first week."),
        ("Do I need a special sales AI tool?", "Not to start. A general assistant with your ideal-customer profile and examples of your best emails covers most of it."),
    ],
))

P.append(dict(
    num="06", slug="career-changers", district="the-station", building="station",
    persona="The Career <em>Changer</em>", persona_plain="The Career Changer",
    sector="Cross-industry transition", country="Spain", status="In progress",
    h1="AI career coaching for career changers",
    title="AI Career Coaching for Career Changers: Turn a Varied Background Into a Case",
    desc="How a career changer uses AI to build an evidence-based job search: salary data, target companies and positioning across three role categories.",
    roles=["Career pivoter", "Cross-industry", "Repositioning"],
    answer="A career changer can use AI to research what target roles really pay and need, shortlist companies, and rewrite a varied background into one clear story. The value is the evidence, not a nicer CV.",
    story=[
        "You've done real work across more than one world, and that variety is an asset. Nobody has shown you how to frame it, so it reads as scattered instead of intentional.",
        "<strong>This isn't a CV polish. It's building an evidence-based case</strong>: market data on what the roles pay and need, and a positioning that turns your background into your edge.",
    ],
    result="A data-backed case across three target role categories, with real salary benchmarks, target company lists, a personal site and tailored positioning for each.",
    day=[
        ("09:00", "You apply to anything that looks close.", "You apply inside three defined categories with real salary ranges."),
        ("11:00", "Your CV tries to say everything.", "A different version per category tells one clear story."),
        ("14:00", "An interview invite: you have one evening to prepare.", "AI research on the company and the interviewer is ready in an hour."),
        ("17:00", "You wonder if your past makes sense to anyone.", "A personal site shows it as a path, not a zigzag."),
        ("20:00", "Another evening scrolling job boards.", "A 30-day plan says what to do tomorrow."),
    ],
    signals=[
        "My background doesn't fit one box and I can't explain it as a strength",
        "I don't want a nicer CV. I want a strategy for where to go next",
        "I don't know what these roles really pay or need",
        "Everyone says leverage AI in the job search, nobody says how",
    ],
    outcomes=[
        "A narrative that turns a varied background into a clear story",
        "Salary ranges and role requirements for your target categories",
        "A shortlist of companies worth targeting, with warm paths in",
        "A concrete plan for the next 30 days",
    ],
    tools=["Claude Projects", "Job board research", "Personal website"],
    faq=[
        ("How can AI help me change careers?", "Use it to research roles and salaries, map your past work to what those roles need, and prepare for interviews. It speeds up the research; you still choose the direction."),
        ("Should I make a different CV for each role?", "Yes, one per role category. AI makes that quick once your full history sits in one project it can draw from."),
        ("Is this for entry-level job seekers?", "No. It works best for people with real experience in more than one field who need to explain the thread that connects it."),
    ],
))

P.append(dict(
    num="07", slug="electricians-and-trades", district="old-town", building="trades",
    persona="The Trades Business <em>Owner</em>", persona_plain="The Trades Business Owner",
    sector="Electrical contracting", country="Australia", status="In progress",
    h1="AI for electricians and trades business owners",
    title="AI for Electricians & Trades Businesses: An Ops Dashboard That Finds Lost Money",
    desc="How an Australian electrical contractor connected AI to job management and accounting to catch unpaid jobs and unworked leads. A day in the life of the trade.",
    roles=["Owner", "General manager", "Office team"],
    answer="A trades business can connect AI to its job management and accounting software to spot unpaid completed jobs, leads nobody followed up and jobs missing notes. The value is in finding leaks, not counting jobs.",
    story=[
        "You run a field team and an office team. Leads come in by email, web form and WhatsApp; jobs live in your job software, money in your accounting tool. You only find out something slipped when a client complains or cash is short.",
        "<strong>One job can be worth more than ten. So the question isn't how many jobs you did.</strong> It's which money is stuck, which lead nobody called, and who on the team needs help.",
    ],
    result="On its first test the AI workspace caught an overdue payment the owner didn't know about; the next found a lead nobody had worked. A weekly real-estate jobs report went from about five minutes to one.",
    day=[
        ("06:30", "Techs head out. You're not sure every job has notes.", "The morning check flags jobs with no diary notes before vans leave."),
        ("09:00", "Work orders arrive as emails and PDFs.", "Each one becomes a job, with the client type set so reports make sense."),
        ("12:00", "Someone says a client hasn't paid. Which one?", "Completed-but-unpaid jobs sit at the top of the dashboard."),
        ("15:00", "A lead from last week went cold.", "Unworked leads are flagged the same day."),
        ("21:00", "You check the business from your phone, again.", "One dashboard, on your phone, built for the owner and the GM."),
    ],
    signals=[
        "I only find out about problems when a client complains",
        "My job software holds everything, but I can't see the picture",
        "I don't care how many jobs we did. I care which ones made money",
        "I run most of the business from my phone",
    ],
    outcomes=[
        "AI connected to your job management and accounting tools",
        "Saved weekly reports per client type, in a minute instead of five",
        "A categorisation rulebook so your data stops lying",
        "A visual dashboard for owner and manager, mobile-first",
    ],
    tools=["ServiceM8", "Xero", "Claude Projects", "WhatsApp Business"],
    faq=[
        ("Can AI connect to ServiceM8 and Xero?", "Yes. In this engagement both were connected to Claude through official connectors, so reports read live job and accounting data instead of exports."),
        ("What should a trades business track with AI?", "Money stuck between 'job done' and 'paid', leads not followed up, jobs with no notes, and jobs with no client type. Volume of jobs matters less."),
        ("Do I need a developer?", "Not to start. Connectors and a well-written project cover the first months. Automation and APIs come later, once you know which reports you actually use."),
    ],
))

P.append(dict(
    num="08", slug="construction-companies", district="old-town", building="facade",
    persona="The Construction Operations <em>Director</em>", persona_plain="The Construction Operations Director",
    sector="Facade & cladding contracting", country="United Kingdom", status="In progress",
    h1="AI for construction operations and health & safety reporting",
    title="AI for Construction Companies: Board Reports, Near Misses & Site Reports",
    desc="How a UK facade contractor's operations director uses AI for board reports, near-miss and health & safety reporting, and site visit write-ups.",
    roles=["Operations director", "H&S lead", "Site manager"],
    answer="Construction teams can use AI to turn site voice notes and health & safety records into written reports, action lists and board summaries. It works when the AI has your company's rules and templates, set up once in a shared workspace.",
    story=[
        "Your company was bought into by a larger group, and with it came corporate reporting: monthly board packs, near-miss records, toolbox talks, site reports. You tried to fix one near-miss form with AI and lost eleven hours and two hundred prompts.",
        "<strong>The issue wasn't effort. It was starting every chat from zero.</strong> A workspace that already knows your company, your templates and your safety rules turns each report into a short review instead of a fight.",
    ],
    result="A company AI workspace is set up with instructions and toolbox talk material; board report and email-thread summaries are running. Next: the monthly health & safety workbook into a board-ready summary.",
    day=[
        ("07:00", "Three sites, three sets of problems, one of you.", "Site walk voice notes become a written report and an action list in Excel."),
        ("10:00", "A near miss needs recording properly.", "The near-miss form fills from your notes, in the company format."),
        ("13:00", "A 40-email thread you need to understand.", "A one-page summary: who decided what, what's open."),
        ("16:00", "Board report due. Numbers scattered across workbooks.", "The monthly H&S workbook becomes the board summary draft."),
        ("19:00", "You're typing reports at the kitchen table.", "You review and send. Done before dinner."),
    ],
    signals=[
        "Corporate reporting arrived and nobody gave me more hours",
        "I've spent whole days fighting AI over one form",
        "I'm not technical. I need it step by step",
        "My site notes never become proper reports in time",
    ],
    outcomes=[
        "A company AI workspace that knows your rules, templates and terms",
        "Voice note to site report plus Excel action summary",
        "Near-miss and toolbox talk records in your format",
        "A monthly board report you edit instead of write",
    ],
    tools=["ChatGPT Projects", "Microsoft 365", "Excel", "Outlook"],
    faq=[
        ("Can AI write construction health and safety reports?", "It can draft them from your notes in your company format. A competent person still reviews and signs. The time saved is in the typing and formatting."),
        ("Why did AI fail when I tried it before?", "Usually because every chat started from zero. A project with your templates, rules and examples saved once gives the AI the context a new colleague would need."),
        ("Do I need to be good with computers?", "No. This engagement goes click by click. The goal is that you can run it alone, not that someone runs it for you."),
    ],
))

P.append(dict(
    num="09", slug="ceo-assistant", district="business-district", building="tower",
    persona="The <em>CEO</em>", persona_plain="The CEO",
    sector="Executive leadership", country="Africa", status="In progress",
    h1="An AI assistant for CEOs",
    title="AI Assistant for CEOs: Sales Reports, Slides and a Daily Briefing",
    desc="How a CEO of a 60-person company in Africa uses AI as a chief-of-staff: slide outlines from hand-drawn sketches, sales reports and a competitor watch.",
    roles=["CEO", "Managing director", "Founder"],
    answer="A CEO gets most from AI as a personal chief-of-staff: one workspace that knows the company, turns rough sketches into slide outlines, summarises sales performance and watches competitors. The CEO still makes every decision.",
    story=[
        "You run a company of around sixty people with a sales team that moves every day. Presentations eat your evenings. The sales numbers you get tell you what happened, not who is performing or which products move.",
        "<strong>You don't need to learn to code. You need AI as a central tool in how you lead.</strong> Two assistants, set up once, carry the company context so every request starts from what you already know.",
    ],
    result="In the first lesson the CEO built two assistants: a Slide Assistant that turns hand-drawn slide sketches into slide outlines, and a CEO Assistant loaded with the company brief, sales report and brochure. Next: a daily per-agent sales report and a regional competitor watch.",
    day=[
        ("07:00", "Yesterday's sales: a total, not a story.", "A briefing: who sold, what sold, what to ask the team."),
        ("09:00", "A board presentation tonight. Blank slides.", "You sketch the slides on paper. The assistant turns the photo into an outline."),
        ("12:00", "A competitor launched something. You heard late.", "A weekly watch on your region and industry."),
        ("15:00", "A partner wants the company story in a page.", "The assistant already knows the brief and brochure. One draft, your edits."),
        ("20:00", "Slides again.", "Time with your family."),
    ],
    signals=[
        "Presentations take my evenings",
        "My reports say what happened, not why",
        "I want AI at the centre of how I work, without becoming technical",
        "I hear about competitors too late",
    ],
    outcomes=[
        "A CEO assistant that knows your company",
        "Slides from your own sketches, in your structure",
        "A richer daily sales report: per person and per product",
        "A regular competitor and industry watch",
    ],
    tools=["Claude Projects", "CRM exports", "Slides", "Web research"],
    faq=[
        ("How can a CEO use AI every day?", "Start with the tasks that eat your evenings, usually presentations and reports. Put the company brief and recent reports in one AI project so every request starts with context."),
        ("Can AI turn hand-drawn sketches into slides?", "Yes. Photograph the sketch, and an assistant with your instructions turns it into a slide-by-slide outline in your structure, ready for design."),
        ("Is my company data safe in an AI assistant?", "Use a business plan that doesn't train on your data, and keep sensitive files to what each assistant needs. We set this up in the first lesson."),
    ],
))

P.append(dict(
    num="10", slug="real-estate-agents", district="market-square", building="agency",
    persona="The Real Estate <em>Agent</em>", persona_plain="The Real Estate Agent",
    sector="Residential real estate", country="United Arab Emirates", status="Result",
    h1="AI for real estate agents",
    title="AI for Real Estate Agents: Fix Your Data, Then Market to Your Contacts",
    desc="How a real estate agent in the UAE fixed lead and listing sync across spreadsheets and AI, then turned 5,000 existing contacts into a marketing plan.",
    roles=["Agent", "Team lead", "Listings manager"],
    answer="Real estate agents get the most from AI when their leads and listings are clean first. With a working spreadsheet-based CRM connected to an AI workspace, the next step is marketing to existing contacts: a brand book, a landing page and messaging campaigns.",
    story=[
        "Your small team runs on spreadsheets and an AI workspace instead of a CRM. Leads, listings and the dashboards for management stopped matching, and nobody trusted the numbers.",
        "<strong>Marketing to 5,000 contacts doesn't work on broken data.</strong> So the first job was fixing the sync. The second is turning those contacts into a campaign people want to read.",
    ],
    result="After the first session the sync between leads, listings and dashboards was largely fixed. The focus moved to marketing to around 5,000 existing contacts: brand book, landing page and a social channel.",
    day=[
        ("09:00", "The leads sheet and the listings sheet disagree.", "One source of truth, synced into the AI workspace."),
        ("11:00", "The weekly summary for management takes hours.", "It builds from the sheets, with numbers you trust."),
        ("13:00", "5,000 contacts, no plan.", "Contacts sorted by buyer, seller and tenant, each with a message."),
        ("16:00", "Messages link nowhere.", "A simple landing page catches every reply."),
        ("18:00", "You post when you remember.", "A social channel with a plan."),
    ],
    signals=[
        "Our sheets and dashboards don't match",
        "We have thousands of contacts and do nothing with them",
        "I don't want another tool to pay for",
        "Management wants numbers I can't trust",
    ],
    outcomes=[
        "Clean sync between leads, listings and reports",
        "Segmented contacts with a message per segment",
        "A brand book and landing page for campaigns",
        "A clear split of what goes to IT, marketing and you",
    ],
    tools=["ChatGPT Workspace", "Google Sheets", "Apps Script", "Canva"],
    faq=[
        ("Can a real estate agent use AI without a CRM?", "Yes, for a small team. Google Sheets plus an AI workspace can work as a light CRM, as long as leads and listings stay in sync."),
        ("How should agents market to old contacts?", "Segment by buyer, seller and tenant, write one useful message per segment, and send people to a simple page that captures replies."),
        ("What's the first AI fix for an agency?", "Data. If leads, listings and reports disagree, every AI summary inherits the error."),
    ],
))

P.append(dict(
    num="11", slug="dental-clinics", district="business-district", building="clinic",
    persona="The Clinic <em>Owner</em>", persona_plain="The Clinic Owner",
    sector="Dental practice", country="United States", status="Getting started",
    h1="AI for dental practice owners",
    title="AI for Dental Practices: Safe Automation for Insurance, SOPs and Meetings",
    desc="How a US dental practice owner plans AI for insurance payments, account adjustments, SOPs and team meetings, starting with fake patient data and HIPAA in mind.",
    roles=["Practice owner", "Office manager", "Team lead"],
    answer="Dental practices can use AI for meeting summaries, SOPs and training manuals right away. Writing into the practice management system, for insurance payments or adjustments, needs a safe setup first: a business agreement covering patient data and testing on fake patients.",
    story=[
        "You own a twelve-person practice that already runs on a clear operating system: weekly meetings, scorecards, goals. You use AI in chat. You want it inside the practice software, posting insurance payments and adjustments, without risking patient data or the system itself.",
        "<strong>The rule is simple: nothing touches real patients until it works on fake ones.</strong> So the first project is a proof of concept on placeholder data, and the patient-data agreement comes before anything goes live.",
    ],
    result="Agreed first project: a proof-of-concept dashboard on fake patients to test the practice software's API safely, while the practice secures a patient-data agreement for its AI tools.",
    day=[
        ("07:30", "Weekly team meeting: notes in a recording nobody reads.", "Agenda and summary from the transcript, in your meeting format."),
        ("10:00", "Insurance payments keyed in by hand.", "Planned: AI drafts the entries, a person approves, on a safe connection."),
        ("13:00", "A new hire needs the procedures.", "SOPs and training manuals drafted from how you actually work."),
        ("15:00", "Overdue accounts in a report you rarely open.", "Planned: a weekly overdue and claim-status summary."),
        ("18:00", "You wonder if AI is safe for a clinic.", "You know what touches patient data and what doesn't."),
    ],
    signals=[
        "I want AI in our practice software, but not at the cost of patient data",
        "Our meetings and SOPs live in recordings and heads",
        "Insurance entries eat front-desk hours",
        "My team doesn't use AI yet",
    ],
    outcomes=[
        "A clear line between what AI can do now and what needs a patient-data agreement",
        "A proof of concept on fake patients before anything touches real data",
        "Meeting agendas, summaries, SOPs and training manuals",
        "A plan to bring the team along",
    ],
    tools=["Claude", "Practice management API", "Meeting transcripts"],
    faq=[
        ("Is AI HIPAA compliant for dental practices?", "It depends on the plan and agreement, not the model. Use a business plan with a signed agreement for patient data, and keep patient data out of consumer tools."),
        ("Can AI post insurance payments into practice software?", "Technically yes, through the software's API. Do it only after testing on fake patients, with a person approving every write."),
        ("What can a clinic use AI for today, safely?", "Meeting agendas and summaries, SOPs, job descriptions and training manuals: anything without patient data."),
    ],
))

P.append(dict(
    num="12", slug="hospitality-software", district="old-town", building="bar",
    persona="The Hospitality Operator Building a <em>SaaS</em>", persona_plain="The Hospitality Operator Building a SaaS",
    sector="Hospitality operations software", country="Spain", status="In progress",
    h1="AI for hospitality operators building their own software",
    title="AI for Hospitality Operators: Build and Own Your Bar Management Software",
    desc="How a hospitality operator in Spain is moving a bar-management app off an expensive no-code platform and turning it into a SaaS for other bars.",
    roles=["Operator", "Consultant", "Founder"],
    answer="Hospitality operators can build their own operations software with AI, but no-code platforms get expensive as usage grows. The usual path is to rebuild one module at a time on your own stack, then package it for other venues.",
    story=[
        "You run operations and accounting for several bars, and you built an app to manage them: finance, budgets, staff, legal, supplier orders. It works and people use it daily. But the no-code platform it runs on costs more every month, and the logic has grown messy.",
        "<strong>The goal isn't just cheaper hosting. It's owning the product</strong>, so it can become software other bars pay for, bundled with the expertise behind it.",
    ],
    result="A first app already runs on its own hosting and database, outside the no-code platform. The plan: halve monthly running costs, rebuild modules one by one, and package an entry tier for other bars.",
    day=[
        ("08:00", "Last night's takings, in three systems.", "Sales and costs land in one weekly report per bar."),
        ("11:00", "Each bar manager asks for their own numbers.", "Managers see only their bar. You see everything."),
        ("14:00", "The no-code bill arrives.", "Modules move to your own stack, one at a time."),
        ("17:00", "Another bar owner asks what you use.", "There's a version you can sell them."),
        ("23:00", "Service. Your phone buzzes with questions.", "The app answers the routine ones."),
    ],
    signals=[
        "My no-code app works, but the bill keeps growing",
        "I'd rebuild it if I knew where to start",
        "Other venues want what we have",
        "Client money data must stay private",
    ],
    outcomes=[
        "A migration plan module by module, not a risky big-bang rebuild",
        "Your own hosting and database",
        "A product tier other venues can buy",
        "Privacy rules for client financial data",
    ],
    tools=["Base44", "Vercel", "Supabase", "Claude Code"],
    faq=[
        ("Can I build bar management software with AI?", "Yes. A working app for finance, staff and orders is realistic. Plan for ownership early: hosting, database and access rules."),
        ("Should I leave my no-code platform?", "When monthly costs and messy logic outweigh speed. Move one module at a time so the bars never stop working."),
        ("How do I turn an internal tool into a SaaS?", "Start with the module other venues ask about most, price an entry tier, and keep your consultancy as the premium layer."),
    ],
))

P.append(dict(
    num="13", slug="accountants", district="business-district", building="bank",
    persona="The <em>Accountant</em>", persona_plain="The Accountant",
    sector="Accounting & audit", country="Europe", status="Getting started",
    h1="AI for accountants building their own audit tools",
    title="AI for Accountants: From Copy-Paste Prompts to Your Own Audit Software",
    desc="How a European accountant is moving from pasting prompts between AI tools to building a structured MVP of her own statutory audit software.",
    roles=["Accountant", "Auditor", "Firm owner"],
    answer="Accountants can use AI to build their own tools, such as audit checklists and anomaly checks, without being programmers. The step that matters is moving from copy-pasting prompts between chats to a structured project with a clear MVP.",
    story=[
        "You want to work less on routine and more on new clients. You've already built a working desktop tool for statutory audits by writing prompts in one AI and pasting them into another.",
        "<strong>It works, but it doesn't scale.</strong> The next step is structure: one place for the logic, a defined MVP, and AI that points at anomalies while you sign the audit.",
    ],
    result="The first lessons define the goal of the software and an MVP structure, so the tool grows on purpose instead of by copy-paste.",
    day=[
        ("09:00", "Ledgers to check, line by line.", "The tool flags anomalies. You review the flags."),
        ("11:00", "A prompt written in one AI, pasted into another.", "One project holds the logic, versions and tests."),
        ("14:00", "A client asks a routine question for the third time.", "A drafted answer, checked by you."),
        ("16:00", "No time for new clients.", "Routine shrinks. New-client hours grow."),
        ("18:00", "Your software lives on one PC.", "An MVP you can show and improve."),
    ],
    signals=[
        "I've built something with AI, but it's held together by copy-paste",
        "I want to go from coworker-level AI to building with code",
        "Routine work leaves no time for new clients",
        "The professional signs, not the AI",
    ],
    outcomes=[
        "A clear MVP for your software",
        "A structured project instead of pasted prompts",
        "AI that flags, you that approve",
        "A path from desktop tool to product",
    ],
    tools=["Claude", "Claude Code", "ChatGPT", "Desktop app"],
    faq=[
        ("Can accountants build software with AI without coding?", "Yes, to a working tool. Structure matters more than code: a defined goal, an MVP and a project where the logic lives."),
        ("Can AI do an audit?", "No. It can flag anomalies and prepare working papers. The accountant reviews and signs."),
        ("What's an MVP for an audit tool?", "The smallest version that does one check end to end on real files, such as matching ledgers to bank statements."),
    ],
))

ORDER = ["01", "07", "08", "12", "09", "02", "11", "13", "03", "04", "05", "10", "06"]
