"""Expanded content for ICP guide pages."""

GUIDE_CONTENT = {}

# =============================================================================
# SDRs & BDRs
# =============================================================================
GUIDE_CONTENT["best-tools-for-sdrs"] = {
 "intro_long": (
 "The SDR role is a volume game with a quality filter. You're making 50-100 touches per day"
 " across email, phone, and LinkedIn, trying to start conversations with people who didn't"
 " ask to hear from you. The reps who book the most meetings have two things in common:"
 " they spend more time talking to prospects and less time finding them, and their outreach"
 " feels personal even at scale. The right tool stack makes both of those possible.\n\n"
 "Your core workflow has four stages: build a list of prospects who match your ICP, run"
 " multi-channel sequences to get their attention, connect with them live on the phone,"
 " and book meetings with the ones who are interested. Each stage has tools purpose-built"
 " for speed. The best SDR stacks automate the low-value steps (finding emails, logging"
 " activities, scheduling meetings) so you can spend your time on the high-value step:"
 " having real conversations with qualified buyers.\n\n"
 "Most SDR teams overspend on tools and underinvest in process. A focused stack of 3-4"
 " tools with strong adoption will outperform a bloated stack of 8 tools that nobody"
 " uses properly. Start with a prospecting database, a sequencing platform, and a dialer."
 " Add scheduling automation once your meeting volume justifies it. Every tool you add"
 " should save your reps at least 30 minutes per day, or it's not worth the onboarding cost."
 ),
 "workflow_overview": (
 "The SDR tool stack flows in a straight line: prospect data feeds into sequencing, sequencing"
 " triggers calls, and calls convert to booked meetings. Your prospecting tool (Apollo,"
 " ZoomInfo, or Lusha) exports contacts directly into your sequencing platform (Outreach,"
 " Salesloft, or Instantly). The sequencing platform orchestrates multi-step campaigns"
 " across email and LinkedIn, while your dialer (Orum, Nooks, or Kixie) handles the phone"
 " channel. When a prospect says yes, your scheduling tool (Calendly or Chili Piper)"
 " eliminates the back-and-forth of finding a time.\n\n"
 "The integrations between these tools matter as much as the tools themselves. Your sequencing"
 " platform should sync activities back to your CRM automatically. Your dialer should log"
 " calls and dispositions without manual data entry. And your scheduling link should update"
 " the CRM record, notify the AE, and trigger any follow-up sequences. A well-integrated"
 " stack means reps never switch tabs to log activities. They prospect, call, book, and move on."
 ),
 "budget_guidance": (
 "A competitive SDR stack costs $200-$500 per rep per month. The prospecting database is"
 " typically the largest line item: Apollo starts at $49/month for individuals but runs"
 " $79-$119/month per user on team plans, while ZoomInfo starts around $15,000/year for"
 " small teams. Sequencing platforms range from $25/month (Instantly) to $100-$150/month"
 " per user (Outreach, Salesloft). Dialers add $50-$150/month per seat. Scheduling tools"
 " are the cheapest layer at $10-$30/month per user.\n\n"
 "For teams with tight budgets, Apollo covers both prospecting and basic sequencing in a"
 " single platform, starting at $49/month. Pair it with Kixie for calling ($35/month) and"
 " Calendly for scheduling (free tier works for most SDRs), and you have a full stack for"
 " under $150/month per rep. Enterprise teams with budget for best-in-class tools typically"
 " run ZoomInfo for data, Outreach or Salesloft for sequencing, and Orum or Nooks for"
 " parallel dialing, landing at $400-$600/month per rep."
 ),
 "implementation_timeline": (
 "A new SDR stack takes 2-4 weeks to deploy. Week one: set up your prospecting database,"
 " import your ICP criteria, and build your first target account list. Week two: configure"
 " your sequencing platform with 2-3 proven sequence templates, connect it to your CRM,"
 " and run a small test campaign. Week three: roll out the dialer, train reps on call"
 " workflows, and integrate scheduling links into email signatures and sequences.\n\n"
 "Resist the urge to launch everything at once. SDRs learn tools by using them in their"
 " daily workflow, and three simultaneous tool rollouts create confusion. Start with the"
 " sequencing platform (they'll use it every day), add the prospecting database once"
 " sequences are running smoothly, then layer in the dialer. Full adoption typically"
 " takes 4-6 weeks from first login to consistent daily usage across the team."
 ),
 "section_details": {
 "Finding Prospects": (
 "Your prospecting database determines the quality and volume of your outbound pipeline."
 " Apollo offers the best value for startups and mid-market teams, with solid contact"
 " data and built-in sequencing at a fraction of ZoomInfo's price. ZoomInfo delivers"
 " the deepest data coverage for enterprise prospecting, with direct dials and org"
 " charts that justify its premium pricing. Lusha provides a lightweight Chrome"
 " extension for quick lookups on LinkedIn. Sales Navigator is essential for LinkedIn-first"
 " prospecting, with advanced filters and InMail credits that complement your email"
 " and phone outreach."
 ),
 "Running Outreach": (
 "Your sequencing platform is the tool you'll live in every day. Outreach and Salesloft"
 " are the enterprise standards, with deep CRM integrations, analytics, and management"
 " visibility. Instantly is the budget-friendly option for email-heavy outbound, with"
 " unlimited email accounts and strong deliverability features. Lemlist adds"
 " personalization capabilities like custom images and landing pages that boost reply"
 " rates on creative campaigns."
 ),
 "Making Calls": (
 "Parallel dialers like Orum and Nooks multiply your connect rate by dialing multiple"
 " prospects simultaneously and connecting you only when someone picks up. An SDR using"
 " a parallel dialer can have 15-25 live conversations per hour compared to 3-5 with"
 " manual dialing. Kixie is a solid single-line power dialer with strong CRM integration"
 " that works well for teams that prefer a simpler calling workflow."
 ),
 "Booking Meetings": (
 "Scheduling friction kills deals that are ready to move forward. Calendly is the most"
 " widely used scheduling tool, with a clean booking experience and solid integrations."
 " Chili Piper goes further with intelligent routing, round-robin distribution, and"
 " instant booking from inbound forms, making it the better choice for teams handling"
 " both inbound and outbound meeting flow."
 ),
 },
 "faqs": [
 {
 "question": "What's the minimum tool stack an SDR needs to be productive?",
 "answer": (
 "Three tools: a prospecting database, a sequencing platform, and a scheduling link."
 " Apollo covers the first two in a single platform, and Calendly's free tier handles"
 " scheduling. You can run effective outbound for under $50/month with this setup."
 " Add a dialer once your call volume justifies the cost."
 ),
 },
 {
 "question": "Should SDRs use Apollo or ZoomInfo for prospecting?",
 "answer": (
 "Apollo for most teams. It offers strong contact data, built-in sequencing, and"
 " pricing that works at any team size. ZoomInfo is worth the premium if you sell"
 " to enterprise accounts and need direct dials, org charts, and intent data."
 " For teams under 10 reps, Apollo delivers 80% of ZoomInfo's value at 20% of the cost."
 ),
 },
 {
 "question": "Do SDRs need a parallel dialer?",
 "answer": (
 "If phone is a primary channel in your outbound motion, yes. Parallel dialers"
 " like Orum and Nooks increase live conversations by 3-5x compared to manual"
 " dialing. The ROI is clear for teams where SDRs are expected to make 50+ dials"
 " per day. For email-first teams that make occasional calls, a basic power dialer"
 " or even the phone on your desk is fine."
 ),
 },
 {
 "question": "How do I measure ROI on my SDR tool stack?",
 "answer": (
 "Track three metrics: meetings booked per rep per week, cost per meeting booked,"
 " and time spent on non-selling activities. A good tool stack should increase"
 " meetings by 30-50% while reducing manual work (data entry, list building,"
 " activity logging) by 5-10 hours per rep per week. Divide your total tool"
 " spend by meetings booked to get cost per meeting."
 ),
 },
 {
 "question": "What's the biggest mistake SDR teams make with their tool stack?",
 "answer": (
 "Buying too many tools and adopting none of them well. A team running Outreach"
 " at 90% adoption will crush a team with Outreach, Salesloft, Apollo sequences,"
 " and Instantly all running at 30% adoption. Pick one tool per function, train"
 " your team properly, and enforce consistent usage before adding anything new."
 ),
 },
 ],
}

# =============================================================================
# Account Executives
# =============================================================================
GUIDE_CONTENT["best-tools-for-aes"] = {
 "intro_long": (
 "Account Executives own the revenue number. Your job is to take qualified opportunities"
 " and convert them into signed contracts, which means every tool in your stack should"
 " either help you run a better sales process or remove friction from the buying process."
 " The best AEs spend their time on discovery calls, building champion relationships,"
 " and navigating procurement. They let tools handle the administrative work: proposals,"
 " contracts, demo follow-ups, and deal room organization.\n\n"
 "The AE tool stack looks different from the SDR stack because the workflow is different."
 " SDRs optimize for volume and speed. AEs optimize for deal progression and close rates."
 " You need your CRM to track pipeline accurately, demo tools to deliver compelling product"
 " experiences, proposal software to create professional quotes quickly, e-signature"
 " platforms to close without delays, and deal rooms to keep multi-stakeholder deals"
 " organized. Each tool maps to a stage in your sales cycle.\n\n"
 "Where most AEs go wrong is treating tools as optional extras rather than process"
 " infrastructure. An AE who sends proposals as email attachments and chases signatures"
 " over email loses deals to competitors who send branded proposals with embedded"
 " e-signatures and real-time tracking. Buyers expect a polished, frictionless experience."
 " Your tools deliver that experience while giving you visibility into buyer engagement"
 " that helps you prioritize the deals most likely to close."
 ),
 "workflow_overview": (
 "The AE workflow moves from discovery to close, and your tools should mirror that"
 " progression. Your CRM (Salesforce, HubSpot, or Pipedrive) is the system of record"
 " where every deal lives. After discovery and qualification, you run demos using"
 " interactive platforms (Storylane, Navattic, or Walnut) that let prospects explore"
 " your product on their own time. When the prospect is ready to buy, your proposal"
 " tool (PandaDoc, Proposify, or Qwilr) generates a professional quote in minutes."
 " The e-signature workflow is embedded in the proposal or handled by a dedicated"
 " platform (DocuSign or HelloSign). Throughout the deal, a digital sales room (Dock,"
 " Aligned, or GetAccept) gives all stakeholders a single place to access content,"
 " track progress, and collaborate.\n\n"
 "The best AE stacks minimize context-switching. PandaDoc, for example, handles both"
 " proposals and e-signatures in one platform. Dock combines deal rooms with mutual"
 " action plans. Look for tools that cover multiple functions well rather than buying"
 " a separate point solution for every step."
 ),
 "budget_guidance": (
 "AE tools typically cost $150-$400 per rep per month on top of your CRM. The CRM itself"
 " is the base layer: Salesforce runs $75-$300/user/month depending on your edition,"
 " HubSpot Sales Hub starts at $45/month, and Pipedrive starts at $14/month. Demo"
 " automation platforms range from $40-$500/month depending on team size and features."
 " Proposal tools cost $20-$65/user/month. E-signature platforms run $15-$45/user/month."
 " Deal rooms are typically $30-$100/user/month.\n\n"
 "For smaller teams, focus your budget on the CRM and one multi-function tool. PandaDoc"
 " at $35/month handles proposals, quotes, and e-signatures in a single platform. Dock"
 " combines deal rooms with mutual action plans at $49/month. A lean AE stack of HubSpot"
 " CRM (free), PandaDoc ($35/month), and Storylane ($40/month) gives you full coverage"
 " for around $75/month per rep. Enterprise teams running Salesforce with Gong,"
 " DocuSign, and a dedicated deal room platform will spend $500+ per rep per month."
 ),
 "implementation_timeline": (
 "Roll out AE tools in order of daily usage. The CRM comes first (it's likely already in"
 " place). Proposal and e-signature tools come next because they directly impact deal"
 " velocity, and most can be configured in a day. Demo automation takes 1-2 weeks to"
 " set up properly because you need to build your demo environments and flows."
 " Deal rooms can be introduced last since they enhance the process rather than enable it.\n\n"
 "Total deployment time for a full AE stack is 3-5 weeks. The biggest bottleneck is"
 " usually demo content creation, where you need product marketing support to build"
 " interactive walkthroughs that match your key use cases. Start with one demo covering"
 " your primary persona and expand from there."
 ),
 "section_details": {
 "Managing Deals": (
 "Your CRM is where pipeline lives and dies. Salesforce is the default for enterprise"
 " sales teams, with unmatched customization and a massive app ecosystem. HubSpot CRM"
 " offers a cleaner interface and faster setup, making it the strong choice for"
 " mid-market teams. Pipedrive is built specifically for pipeline-driven selling, with"
 " a visual deal board that AEs find intuitive from day one."
 ),
 "Running Demos": (
 "Interactive demo platforms let you build click-through product experiences that"
 " prospects explore on their own. Storylane is the most approachable, with fast"
 " demo creation and strong analytics. Navattic specializes in embedding interactive"
 " demos on your website for product-led growth motions. Walnut offers the deepest"
 " customization for demos tailored to specific accounts and personas."
 ),
 "Creating Proposals": (
 "Proposal tools replace the PDF-attached-to-email approach with trackable, branded"
 " documents that include pricing tables, e-signatures, and analytics. PandaDoc is"
 " the most popular option, with a template library and CRM integrations that let"
 " AEs build proposals in under 10 minutes. Proposify focuses on design-forward"
 " proposals for teams where presentation matters. Qwilr creates web-based proposals"
 " that look like custom microsites."
 ),
 "Getting Signatures": (
 "E-signature platforms remove the last source of friction in the buying process."
 " DocuSign is the enterprise standard with broad legal compliance and recognition."
 " PandaDoc includes e-signatures alongside its proposal features, making it a"
 " two-in-one solution. HelloSign (now Dropbox Sign) offers a simple, affordable"
 " option that works well for straightforward contracts."
 ),
 "Deal Rooms": (
 "Digital sales rooms give buyers and sellers a shared workspace for complex deals."
 " Dock combines deal rooms with mutual action plans and is the strongest option"
 " for enterprise AEs running multi-stakeholder deals. Aligned focuses on buyer"
 " engagement analytics, showing you exactly which stakeholders viewed which content."
 " GetAccept blends deal rooms with e-signatures and video messaging for a more"
 " interactive selling experience."
 ),
 },
 "faqs": [
 {
 "question": "What CRM should an AE team use?",
 "answer": (
 "Salesforce if you need deep customization, complex forecasting, or sell to"
 " enterprise accounts with long sales cycles. HubSpot if you want faster setup,"
 " better UX, and a unified marketing-sales platform. Pipedrive if you have a"
 " straightforward sales process and want the best pipeline visualization at"
 " a low price point."
 ),
 },
 {
 "question": "Are interactive demo platforms worth the investment?",
 "answer": (
 "Yes, for teams where product demos are central to the sales process. Interactive"
 " demos let prospects explore your product at their own pace, which increases"
 " engagement and shortens time-to-value. They also reduce the number of live"
 " demo calls needed, freeing AE time for higher-value conversations. Teams"
 " using interactive demos report 20-40% higher demo-to-close conversion rates."
 ),
 },
 {
 "question": "Should I use PandaDoc for both proposals and e-signatures?",
 "answer": (
 "If proposal creation is a regular part of your workflow, yes. PandaDoc handles"
 " both well and eliminates the need for a separate e-signature tool. If you"
 " mostly send simple contracts that don't need a full proposal builder, a"
 " standalone e-signature tool like DocuSign or HelloSign is simpler and cheaper."
 ),
 },
 {
 "question": "When do deal rooms make sense?",
 "answer": (
 "Deal rooms pay off in complex B2B sales with 3+ stakeholders, deal cycles"
 " longer than 30 days, and multiple content assets shared during the process."
 " If you sell a $5K product with a single decision-maker and a one-call close,"
 " a deal room adds overhead without value. If you sell $50K+ solutions to"
 " buying committees, a deal room keeps everyone aligned and gives you visibility"
 " into stakeholder engagement."
 ),
 },
 {
 "question": "How do I reduce deal cycle time with my tool stack?",
 "answer": (
 "Focus on removing buyer friction. Send interactive demos immediately after"
 " discovery so prospects can share them internally. Use proposals with embedded"
 " e-signatures so the buyer can review and sign in one click. Set up a deal room"
 " early so stakeholders access content without waiting for email forwards."
 " Each day you shave off the deal cycle compounds across your pipeline."
 ),
 },
 ],
}

# =============================================================================
# Sales Managers
# =============================================================================
GUIDE_CONTENT["best-tools-for-sales-managers"] = {
 "intro_long": (
 "Sales managers sit between two audiences: the reps they coach and the leadership they"
 " report to. The tools you need serve both directions. Downward, you need coaching"
 " platforms and call intelligence to help reps improve. Upward, you need pipeline"
 " analytics and performance dashboards to give leadership an accurate forecast. The"
 " managers who hit their team number consistently have strong tools in both categories.\n\n"
 "The biggest lever a sales manager pulls is coaching. A 10% improvement in your weakest"
 " rep's close rate moves the team number more than a 10% improvement in your best rep's"
 " close rate. Conversation intelligence tools like Gong make coaching scalable by recording"
 " every call, identifying patterns in winning deals, and flagging calls where reps need"
 " help. Without these tools, coaching relies on ride-alongs and pipeline reviews, which"
 " cover maybe 5% of your team's actual selling conversations.\n\n"
 "Pipeline management is the other half of the equation. You need to know which deals"
 " are real, which are stuck, and which are at risk, and you need that picture updated"
 " daily without chasing reps for CRM updates. Revenue intelligence platforms like Clari"
 " pull pipeline data from emails, calls, and calendar events to build a forecast that"
 " reflects reality rather than rep optimism. Paired with performance dashboards that"
 " track leading indicators (activities, conversations, pipeline creation), you can spot"
 " problems before they become missed quarters."
 ),
 "workflow_overview": (
 "A sales manager's tool stack feeds a weekly rhythm: review calls, coach reps, inspect"
 " pipeline, and report up. Your conversation intelligence platform (Gong or a coaching"
 " tool like Mindtickle) captures every rep interaction and surfaces the ones that need"
 " your attention. Performance dashboards (Atrium, Kluster, or Salesforce reports) show"
 " you which reps are trending behind and why. Revenue intelligence (Clari or Gong Forecast)"
 " gives you pipeline accuracy for your weekly forecast submission. Your engagement platform"
 " (Outreach or Salesloft) shows team-level outreach metrics and lets you monitor sequence"
 " performance across all reps.\n\n"
 "The key is connecting these tools into a single operating cadence. Monday: review Clari"
 " for pipeline changes and flag at-risk deals. Tuesday through Thursday: pull Gong call"
 " highlights to prep for 1:1 coaching sessions. Friday: review Atrium dashboards for"
 " weekly activity metrics and send performance summaries. This rhythm works when your"
 " tools feed each other data, so invest in CRM integrations that keep everything in sync."
 ),
 "budget_guidance": (
 "Sales manager tools are typically purchased at the team or org level rather than per-seat."
 " Gong is the largest investment, running $100-$150 per user per month with annual"
 " contracts (and the pricing covers your reps, too). Revenue intelligence platforms like"
 " Clari typically run $50-$100/user/month. Performance dashboards like Atrium start around"
 " $500/month for a team. Engagement platforms (Outreach, Salesloft) are usually already in"
 " the stack for your reps.\n\n"
 "For a team of 10 reps plus a manager, expect $2,000-$5,000/month for a full management"
 " tool stack on top of existing CRM and sequencing costs. The ROI case is straightforward:"
 " if better coaching and pipeline visibility help one additional rep hit quota each quarter,"
 " the tool investment pays for itself many times over. Start with conversation intelligence"
 " (it provides the most immediate coaching value), then add pipeline analytics and"
 " performance dashboards as your management process matures."
 ),
 "implementation_timeline": (
 "Conversation intelligence (Gong, Mindtickle) deploys in 1-2 weeks. Connect it to your"
 " video conferencing and phone systems, and it starts recording automatically. The real"
 " timeline is building the coaching habit: plan 3-4 weeks for managers to establish a"
 " consistent call review and feedback cadence. Pipeline management tools (Clari) integrate"
 " with your CRM in about a week but need 2-3 weeks of historical data to produce"
 " meaningful forecasts.\n\n"
 "Performance dashboards require the most configuration time because they need custom"
 " metrics and thresholds for your specific team. Budget 2-3 weeks to set up dashboards"
 " that reflect your actual KPIs. The complete management stack is fully operational in"
 " 6-8 weeks, with the first 2 weeks focused on technical setup and the remaining weeks"
 " on adoption and process integration."
 ),
 "section_details": {
 "Coaching Reps": (
 "Gong is the gold standard for conversation intelligence, recording every call and"
 " surfacing coaching moments with AI-powered analysis. Mindtickle goes beyond call"
 " recording into structured training programs with certifications, quizzes, and"
 " skill assessments. Second Nature provides AI role-play simulations where reps"
 " practice pitches and objection handling with an AI buyer before live calls."
 ),
 "Tracking Performance": (
 "Atrium automatically detects performance anomalies across your team, alerting you"
 " when a rep's activity drops or a metric trends in the wrong direction. Kluster"
 " provides pipeline analytics and forecasting with a strong visual interface."
 " Salesforce Reports and Dashboards offer basic performance tracking that works"
 " well enough for teams already deep in the Salesforce ecosystem."
 ),
 "Managing Pipeline": (
 "Clari is the leading revenue intelligence platform, using AI to analyze pipeline"
 " signals from CRM, email, and calendar data. It gives managers a forecast they"
 " can trust without relying on rep self-reporting. Gong Forecast brings Gong's"
 " conversation data into the forecasting equation, predicting deal outcomes based"
 " on actual buyer engagement patterns observed in calls and emails."
 ),
 "Running Outreach": (
 "Your engagement platform is where your reps spend most of their day, which makes"
 " it a critical management visibility tool. Outreach and Salesloft provide team-level"
 " analytics on email performance, call activity, and sequence conversion rates."
 " Apollo Engagement offers similar sequencing capabilities at a lower price point,"
 " making it a practical option for teams where the full Outreach/Salesloft feature"
 " set exceeds their needs."
 ),
 },
 "faqs": [
 {
 "question": "Is Gong worth the price for a small sales team?",
 "answer": (
 "For teams of 5+ reps, yes. The coaching insights and deal intelligence pay for"
 " themselves quickly. For teams under 5, the per-seat cost is harder to justify."
 " Consider Fireflies.ai or Otter.ai for basic call recording at a fraction of"
 " the price, and invest in Gong when your team grows."
 ),
 },
 {
 "question": "How do I get reps to use the tools I buy?",
 "answer": (
 "Tie tool usage to your management process. If you coach from Gong call recordings"
 " in every 1:1, reps will update their calls. If you run pipeline reviews from"
 " Clari instead of asking reps to self-report, they'll keep their deals updated."
 " Tools get adopted when they're embedded in how the team operates, not when you"
 " send a Slack message saying everyone needs to start using them."
 ),
 },
 {
 "question": "What metrics should I track in my performance dashboard?",
 "answer": (
 "Leading indicators: daily activities (calls, emails, meetings booked), pipeline"
 " created per week, and new opportunities added. Lagging indicators: win rate,"
 " average deal size, cycle time, and quota attainment. The leading indicators tell"
 " you where problems are forming. The lagging indicators confirm the result."
 " Track both, but act on the leading indicators."
 ),
 },
 {
 "question": "Do I need separate tools for forecasting and pipeline management?",
 "answer": (
 "Clari handles both in a single platform, and for most teams that's sufficient."
 " Gong Forecast adds call-level signals to your pipeline analysis, which helps"
 " if your forecast accuracy needs improvement. If you're already using Gong for"
 " conversation intelligence, adding Gong Forecast keeps everything in one ecosystem."
 ),
 },
 {
 "question": "What's the most impactful tool investment for a new sales manager?",
 "answer": (
 "Conversation intelligence, every time. Gong or a similar platform gives you"
 " instant visibility into what your reps are saying on calls, which"
 " is the foundation of effective coaching. You can manage pipeline with"
 " spreadsheets and run reports from your CRM, but there's no manual substitute"
 " for reviewing recorded calls at scale."
 ),
 },
 ],
}

# =============================================================================
# VPs of Sales & CROs
# =============================================================================
GUIDE_CONTENT["best-tools-for-vps-cros"] = {
 "intro_long": (
 "Revenue leaders are judged on one thing: did you hit the number? Every tool decision"
 " you make should connect back to forecast accuracy, pipeline health, and team"
 " productivity. You're making buying decisions that affect 50-500 people and six-figure"
 " annual budgets, so the stakes of picking the wrong tool are higher at this level"
 " than anywhere else in the org.\n\n"
 "The VP/CRO tool stack centers on visibility and prediction. You need to call your"
 " number with confidence by Thursday of the last week of the quarter. That requires"
 " a forecasting platform that goes beyond pipeline math, conversation intelligence"
 " that tells you what's happening in deals your managers aren't surfacing, and intent"
 " data that shows you where future pipeline will come from. These tools replace gut"
 " feel with data, which matters when your board expects precision.\n\n"
 "Commission management deserves a spot in the revenue leader's toolkit because comp"
 " drives behavior. If your comp plans are calculated in spreadsheets, your reps don't"
 " trust the numbers, disputes eat manager time, and top performers leave because they"
 " think they're being underpaid. Modern commission platforms give reps real-time"
 " visibility into their earnings, automate plan calculations across complex structures,"
 " and free up finance and ops teams from manual spreadsheet work. The behavioral impact"
 " of transparent, accurate comp is one of the highest-ROI tool investments you can make."
 ),
 "workflow_overview": (
 "The CRO's tool stack operates at the strategic layer. Your CRM (Salesforce or HubSpot)"
 " is the foundation where all revenue data lives. Your forecasting platform (Clari, Gong"
 " Forecast, or Aviso) sits on top of the CRM and analyzes pipeline signals to produce"
 " an AI-driven forecast you can present to the board. Conversation intelligence (Gong"
 " or Chorus) gives you deal-level insight without requiring you to sit in on calls."
 " Intent data (6sense, Bombora, or Demandbase) shows which accounts are researching"
 " your category, feeding your demand gen and outbound teams with in-market signals.\n\n"
 "These tools connect to form a revenue operating system. Intent data identifies accounts"
 " showing buying signals. Your teams engage those accounts through CRM-orchestrated"
 " motions. Conversation intelligence captures deal interactions and surfaces risks. Your"
 " forecasting platform aggregates all of this into a number you can commit to."
 " Commission management (CaptivateIQ, Spiff, or QuotaPath) ensures your team's"
 " compensation accurately reflects their contribution, closing the loop between"
 " strategy and execution."
 ),
 "budget_guidance": (
 "Revenue leader tools carry the highest price tags in the sales stack, reflecting their"
 " org-wide impact. Salesforce Enterprise runs $165/user/month. Clari starts around"
 " $50-$100/user/month with enterprise minimums. Gong at $100-$150/user/month covers"
 " your entire selling org. Intent data platforms (6sense, Bombora, Demandbase) start at"
 " $25,000-$50,000/year. Commission management platforms range from $15-$40/user/month."
 " A full CRO stack for a 100-person revenue org can run $500,000-$1,000,000+ per year.\n\n"
 "Prioritize based on your biggest gap. If you're missing forecast accuracy, start with"
 " Clari. If you're blind to deal quality, start with Gong. If your pipeline is"
 " unpredictable, invest in intent data. If comp disputes are burning manager time and"
 " causing attrition, fix commission management first. You don't need all of these at"
 " once, but you'll likely layer them all in within 12-18 months of taking the role."
 ),
 "implementation_timeline": (
 "CRO-level tools have the longest implementation timelines because they touch multiple"
 " teams and systems. CRM migration (if needed) takes 2-6 months depending on complexity."
 " Forecasting platforms deploy in 4-6 weeks but need a full quarter of data to produce"
 " reliable predictions. Conversation intelligence deploys in 2-3 weeks technically, but"
 " adoption across the org takes 1-2 months. Intent data platforms take 4-8 weeks to"
 " implement and tune to your ICP.\n\n"
 "Commission management has the most variable timeline: simple plans deploy in 2-4 weeks,"
 " while complex multi-variable plans with accelerators, SPIFs, and team overrides can"
 " take 8-12 weeks to configure and validate. Plan tool rollouts around fiscal year"
 " boundaries when possible, especially for forecasting and commission platforms."
 ),
 "section_details": {
 "Revenue Forecasting": (
 "Clari is the category leader in revenue forecasting, using AI to analyze pipeline"
 " signals, deal progression, and historical patterns. It replaces the spreadsheet-based"
 " forecast roll-up with an automated, signal-driven prediction. Gong Forecast"
 " incorporates conversation data into deal predictions, identifying risks based on"
 " buyer engagement in actual calls. Aviso brings multi-model AI forecasting and is"
 " strong in large enterprise environments with complex go-to-market motions."
 ),
 "CRM": (
 "At the CRO level, CRM selection is a strategic decision that shapes your entire"
 " go-to-market operation. Salesforce is the default for enterprise, with unmatched"
 " customization, AppExchange ecosystem, and the ability to support complex sales"
 " processes. HubSpot CRM is gaining ground with revenue leaders who value faster"
 " deployment, better UX, and a unified platform across marketing, sales, and service."
 ),
 "Conversation Intelligence": (
 "Gong dominates conversation intelligence with the deepest analytics, AI-driven deal"
 " insights, and the largest market share. Revenue leaders use Gong to inspect deal"
 " health across the entire org without joining calls. Chorus (owned by ZoomInfo)"
 " offers solid conversation analytics with tighter ZoomInfo data integration, making"
 " it a natural fit for teams already invested in the ZoomInfo ecosystem."
 ),
 "Intent Data": (
 "Intent data platforms tell you which accounts are actively researching your category"
 " or competitors. 6sense is the most comprehensive, combining intent data with"
 " predictive analytics and account-based advertising. Bombora provides the largest"
 " intent data co-op, aggregating signals from thousands of B2B publisher websites."
 " Demandbase blends intent data with advertising and account-based marketing in a"
 " single platform."
 ),
 "Commission Management": (
 "CaptivateIQ handles complex enterprise comp plans with support for multi-variable"
 " calculations, accelerators, and cross-team crediting. Spiff focuses on real-time"
 " commission visibility for reps, with a clean mobile interface that lets sellers"
 " check their earnings after every deal. QuotaPath offers the most affordable entry"
 " point for startups and mid-market teams that need to move off spreadsheet-based"
 " comp calculations."
 ),
 },
 "faqs": [
 {
 "question": "What's the most important tool for a new VP of Sales to buy first?",
 "answer": (
 "A forecasting platform. You need to call your number accurately from day one,"
 " and inherited pipeline is notoriously unreliable. Clari or Gong Forecast gives"
 " you an objective view of pipeline health within your first month, which is"
 " critical for building credibility with your board."
 ),
 },
 {
 "question": "Is intent data worth the investment?",
 "answer": (
 "For companies with an outbound or ABM motion, yes. Intent data identifies accounts"
 " 6-12 months before they enter a buying cycle, letting you engage them before"
 " competitors. The typical ROI calculation: if intent data helps you source 10"
 " additional enterprise deals per year, it pays for itself several times over."
 " For pure inbound businesses, the value is lower."
 ),
 },
 {
 "question": "Should I consolidate on Salesforce or HubSpot?",
 "answer": (
 "Salesforce if you have complex sales processes, need deep customization, or sell"
 " to enterprise accounts. HubSpot if you want faster time-to-value, cleaner UX,"
 " and a unified platform with marketing. The switching cost between them is high,"
 " so this decision should be made for a 3-5 year horizon."
 ),
 },
 {
 "question": "How do I justify six-figure tool investments to my CFO?",
 "answer": (
 "Tie every tool to a revenue metric the CFO cares about. Forecasting tools reduce"
 " forecast error by 15-30%, which directly impacts planning accuracy. Conversation"
 " intelligence increases win rates by 5-15% through better coaching. Intent data"
 " improves pipeline conversion by identifying in-market accounts. Quantify the"
 " revenue impact at your average deal size and let the math make the case."
 ),
 },
 {
 "question": "Do I need both Gong and Clari?",
 "answer": (
 "They solve different problems. Gong tells you what's happening in deals at the"
 " conversation level. Clari tells you what's happening across your pipeline at"
 " the forecast level. Many revenue orgs run both: Gong for deal inspection and"
 " coaching, Clari for forecast accuracy and pipeline analytics. If budget forces"
 " a choice, pick based on your bigger gap."
 ),
 },
 ],
}

# =============================================================================
# RevOps
# =============================================================================
GUIDE_CONTENT["best-tools-for-revops"] = {
 "intro_long": (
 "RevOps is the operational backbone of the revenue organization. You own the systems,"
 " the data, the processes, and the reporting that the entire go-to-market team depends on."
 " Your tool decisions ripple across sales, marketing, and customer success, which makes"
 " integration, data quality, and scalability your top criteria. A tool that works great"
 " in isolation but doesn't sync properly with your CRM creates more work than it saves.\n\n"
 "The RevOps stack is broader than any other role's because your scope spans the full"
 " revenue lifecycle. You manage data enrichment to keep the CRM clean, CRM administration"
 " to keep the system of record healthy, revenue intelligence for forecasting and pipeline"
 " analytics, CPQ for pricing and quoting, commission management for comp plans, and"
 " analytics for reporting that goes beyond what the CRM natively provides. Each category"
 " has 2-4 tools worth evaluating, and the right combination depends on your company's"
 " size, sales motion, and existing tech stack.\n\n"
 "The biggest challenge RevOps teams face is tool sprawl. Sales leaders buy tools"
 " to solve immediate problems without considering integration or data flow implications."
 " RevOps inherits those tools and has to make them work together. The best RevOps teams"
 " take a platform-first approach: pick strong foundational tools (CRM, enrichment,"
 " analytics) and build integrations between them rather than buying point solutions for"
 " every request. Every tool in your stack should have a clear API, solid CRM integration,"
 " and a data model that plays well with your reporting infrastructure."
 ),
 "workflow_overview": (
 "The RevOps tech stack forms a data pipeline. Enrichment tools (Clay, Clearbit, FullEnrich)"
 " feed clean, complete data into your CRM (Salesforce or HubSpot). The CRM serves as the"
 " system of record that connects to everything else. Revenue intelligence (Clari,"
 " InsightSquared) pulls pipeline data from the CRM and layers on predictive analytics."
 " CPQ (Salesforce CPQ, DealHub, HubSpot CPQ) connects to the CRM for quote generation."
 " Commission management (CaptivateIQ, Spiff, Xactly) reads closed-won data to calculate"
 " comp. Analytics tools (Coefficient, Domo, Kluster) aggregate data across all systems for"
 " cross-functional reporting.\n\n"
 "The integration layer is where RevOps earns its keep. Every tool needs to write clean data"
 " back to the CRM, deduplicate properly, and respect your data model. Build your stack"
 " from the CRM outward: get the CRM right first, then add tools that integrate natively."
 " Avoid tools that require middleware like Zapier for core CRM sync. That's a fragile"
 " connection for mission-critical data flow."
 ),
 "budget_guidance": (
 "RevOps tool budgets vary wildly by company size. A startup with 10 sellers might spend"
 " $2,000-$5,000/month on the full stack. An enterprise with 200 sellers can easily spend"
 " $50,000-$100,000/month. The CRM is the largest line item: Salesforce Enterprise at"
 " $165/user/month for 200 users is $396,000/year just for the CRM. HubSpot's Professional"
 " tier offers similar functionality at roughly 40-60% of Salesforce's cost for mid-market"
 " teams.\n\n"
 "Enrichment tools run $100-$2,000/month depending on volume and provider. Revenue"
 " intelligence is $50-$100/user/month. CPQ ranges from $0 (HubSpot CPQ, included with"
 " Sales Hub Enterprise) to $75/user/month (Salesforce CPQ). Commission management runs"
 " $15-$40/user/month. Analytics tools range from free (Coefficient's starter tier) to"
 " $5,000+/month (Domo enterprise). Prioritize spending on the CRM and enrichment first."
 " Those two investments have the most downstream impact on every other system."
 ),
 "implementation_timeline": (
 "RevOps tools have the longest implementation timelines because they affect the entire"
 " organization. CRM deployment or migration takes 2-6 months. Enrichment tools deploy"
 " in 1-2 weeks but need ongoing tuning for data quality rules. CPQ implementation is"
 " the most complex at 4-12 weeks depending on pricing model complexity. Commission"
 " management takes 3-8 weeks depending on plan complexity. Analytics tools deploy in"
 " 1-3 weeks for basic dashboards.\n\n"
 "Don't try to overhaul the entire stack at once. Sequence your rollouts: CRM first,"
 " enrichment second, then layer in revenue intelligence, CPQ, commissions, and analytics"
 " over 2-3 quarters. Each tool needs time for adoption and process integration before"
 " adding the next one. The total timeline for a comprehensive RevOps stack overhaul is"
 " typically 6-12 months."
 ),
 "section_details": {
 "Data Enrichment": (
 "Clean, complete CRM data is the foundation everything else depends on. Clay provides"
 " waterfall enrichment across 75+ data providers, delivering the highest coverage rates"
 " in the market. Clearbit (now part of HubSpot Breeze Intelligence) offers real-time"
 " firmographic and technographic enrichment that works best for HubSpot customers."
 " FullEnrich is the affordable option for teams that need straightforward email and"
 " phone enrichment without the complexity of a full orchestration platform."
 ),
 "CRM": (
 "RevOps lives in the CRM more than anyone else in the org. Salesforce offers the"
 " deepest customization with custom objects, flows, and an AppExchange ecosystem of"
 " thousands of integrations. HubSpot CRM provides a more streamlined experience with"
 " faster administration and a unified platform that reduces tool sprawl across"
 " marketing, sales, and service teams."
 ),
 "Revenue Intelligence": (
 "Clari is the market leader, providing AI-driven revenue forecasting that goes far"
 " beyond CRM reports. It pulls signals from email, calendar, and CRM activity to"
 " predict deal outcomes and pipeline health. InsightSquared offers strong analytics"
 " and historical reporting that helps RevOps teams identify trends and benchmark"
 " performance across quarters."
 ),
 "CPQ": (
 "Configure-price-quote tools eliminate manual quoting in spreadsheets and reduce"
 " pricing errors. Salesforce CPQ (now Revenue Cloud) integrates deeply with Salesforce"
 " but carries significant implementation complexity. DealHub CPQ offers a more modern"
 " interface with guided selling workflows and faster deployment. HubSpot CPQ is"
 " included with Sales Hub Enterprise and handles straightforward quoting needs for"
 " HubSpot-centric teams."
 ),
 "Commission Management": (
 "CaptivateIQ handles the most complex enterprise comp plans with multi-variable"
 " calculations and strong audit trails. Spiff focuses on real-time earnings"
 " visibility and rep-facing dashboards that reduce comp-related support tickets."
 " Xactly is the legacy enterprise player with deep analytics and benchmarking data"
 " from thousands of comp plans across industries."
 ),
 "Analytics": (
 "Coefficient brings CRM and revenue data directly into Google Sheets and Excel,"
 " making it the fastest path to custom reports for teams comfortable with"
 " spreadsheets. Domo is a full enterprise BI platform that aggregates data across"
 " CRM, marketing automation, finance, and operations systems. Kluster focuses"
 " specifically on revenue analytics and forecasting with a clean interface built"
 " for sales and RevOps teams."
 ),
 },
 "faqs": [
 {
 "question": "How do I evaluate whether a new tool fits our stack?",
 "answer": (
 "Three criteria: native CRM integration (does it sync bi-directionally with your"
 " CRM without middleware?), data model compatibility (does it create clean records"
 " that match your schema?), and API quality (can you automate workflows and extract"
 " data programmatically?). If a tool fails any of these, the integration overhead"
 " will eat the productivity gains."
 ),
 },
 {
 "question": "Should RevOps own the entire sales tech stack?",
 "answer": (
 "Yes. RevOps should own procurement, implementation, and ongoing administration"
 " of every revenue tool. When sales leaders buy tools independently, you end up"
 " with duplicate functionality, broken integrations, and dirty CRM data. Establish"
 " a tool evaluation process that routes all purchase requests through RevOps"
 " for technical review before approval."
 ),
 },
 {
 "question": "How many tools is too many?",
 "answer": (
 "The average sales team uses 10-15 tools. If you're above 15, audit for overlap"
 " and unused licenses. The goal is the minimum number of tools that covers every"
 " critical function with strong integration between them. Each additional tool"
 " adds maintenance burden, training requirements, and potential data sync issues."
 " Cut anything with less than 70% adoption."
 ),
 },
 {
 "question": "What's the best enrichment approach for RevOps?",
 "answer": (
 "Waterfall enrichment through Clay or a similar orchestration tool. No single data"
 " provider has complete coverage, so cascading through multiple providers in"
 " sequence delivers 30-50% more valid contact data than any single source. Set up"
 " automated enrichment triggers in your CRM so new leads get enriched on entry"
 " without manual intervention."
 ),
 },
 {
 "question": "How do I measure the ROI of our tech stack?",
 "answer": (
 "Track tool-specific metrics monthly: CRM data completeness (enrichment), forecast"
 " accuracy (revenue intelligence), quote turnaround time (CPQ), comp dispute"
 " volume (commission management), and report creation time (analytics). Compare"
 " each tool's annual cost against the time it saves and revenue it influences."
 " Kill tools that can't demonstrate measurable impact after two quarters."
 ),
 },
 ],
}

# =============================================================================
# Sales Enablement Leaders
# =============================================================================
GUIDE_CONTENT["best-tools-for-enablement"] = {
 "intro_long": (
 "Sales enablement sits at the intersection of content, training, and process. Your job"
 " is to make every rep as effective as your best rep, and you do that by giving them the"
 " right content, the right training, and the right tools at the right moment in the"
 " sales cycle. The enablement tool stack supports all three: content management systems"
 " that organize and distribute sales assets, coaching platforms that develop rep skills,"
 " and buyer-facing tools that improve the prospect experience.\n\n"
 "The enablement function has matured significantly in the last few years. It used to mean"
 " building slide decks and running onboarding bootcamps. Now it means operating a"
 " content engine that serves reps with context-aware recommendations, running ongoing"
 " coaching programs with measurable skill development, deploying interactive demos that"
 " prospects can explore independently, and managing digital sales rooms that keep"
 " complex deals organized. The tooling has caught up with the ambition of the role.\n\n"
 "The biggest trap for enablement leaders is buying tools that reps won't use. A $50,000"
 " content management platform that reps bypass in favor of Google Drive is a failed"
 " investment. The tools that get adopted share two qualities: they're embedded in the"
 " rep's existing workflow (appearing inside the CRM or sequencing platform, not in a"
 " separate tab), and they provide immediate value (surfacing the right case study for"
 " this specific deal, not requiring 10 clicks to find it). Evaluate every enablement"
 " tool through the lens of rep adoption, because usage determines impact."
 ),
 "workflow_overview": (
 "The enablement stack serves two audiences: reps who need content and training, and"
 " buyers who interact with your materials during the sales process. Your content management"
 " platform (Highspot, Seismic, Showpad, or Guru) is the central hub where all sales"
 " assets live. It integrates with your CRM and email to recommend relevant content based"
 " on deal stage, industry, and persona. Your coaching platform (Mindtickle, Allego, or"
 " SalesHood) runs onboarding programs, ongoing skill development, and certification"
 " tracks that keep reps sharp.\n\n"
 "On the buyer-facing side, demo automation tools (Storylane, Navattic, or Consensus) let"
 " prospects explore your product without scheduling a live call, and digital sales rooms"
 " (Dock, Aligned, or Trumpet) give buyers a branded workspace with all relevant"
 " content, stakeholder information, and next steps in one place. The best enablement"
 " stacks connect these tools so that content performance data flows back into your"
 " analytics, showing you which assets drive pipeline and which ones collect dust."
 ),
 "budget_guidance": (
 "Enablement tools are typically purchased at the org level with annual contracts."
 " Content management platforms are the biggest line item: Highspot and Seismic run"
 " $30-$60/user/month with enterprise minimums that start around $30,000-$50,000/year."
 " Showpad offers a more affordable entry point for mid-market teams. Guru provides"
 " knowledge management at $10-$15/user/month. Coaching platforms range from $20-$60"
 " /user/month. Demo automation runs $40-$500/month depending on usage. Digital sales"
 " rooms cost $30-$100/user/month.\n\n"
 "For teams building an enablement stack from scratch, start with a content management"
 " platform (it's the foundation) and a coaching tool (it drives the most measurable"
 " rep improvement). Demo automation and digital sales rooms can be layered in as the"
 " program matures. A mid-market enablement stack for 50 reps typically runs"
 " $50,000-$120,000/year. Enterprise teams with Highspot or Seismic as the anchor can"
 " spend $200,000-$400,000/year across all enablement tools."
 ),
 "implementation_timeline": (
 "Content management platforms take 4-8 weeks to implement properly. The technical setup"
 " is 1-2 weeks, but migrating content from scattered Google Drives, SharePoint folders,"
 " and Slack channels into a structured taxonomy takes real effort. Plan 2-3 weeks for"
 " content audit and migration, then 2-3 weeks for rep training and adoption. Coaching"
 " platforms deploy in 2-4 weeks, with the main effort going into building your first"
 " onboarding track and certification program.\n\n"
 "Demo automation tools take 1-3 weeks depending on how many demo flows you need to build."
 " Digital sales rooms can launch in 1-2 weeks with basic templates. The full enablement"
 " stack reaches operational maturity in about 3 months. The first month is setup and"
 " content migration, the second month is rep training and adoption, and the third month"
 " is optimization based on usage data and rep feedback."
 ),
 "section_details": {
 "Content Management": (
 "Highspot is the market leader, with AI-powered content recommendations that surface"
 " the right asset based on deal context. It integrates deeply with Salesforce and"
 " Outreach, embedding content suggestions directly in the rep's workflow. Seismic"
 " offers comparable features with strong analytics and content personalization"
 " capabilities. Showpad provides a more accessible entry point for mid-market teams"
 " with solid content organization and buyer engagement tracking. Guru specializes"
 " in knowledge management, providing a wiki-like experience for sales playbooks,"
 " competitive cards, and process documentation."
 ),
 "Coaching & Training": (
 "Mindtickle is the most comprehensive coaching platform, combining onboarding"
 " programs, ongoing training, certifications, and AI-powered role-play into a single"
 " system. Allego focuses on video-based coaching where reps record practice pitches"
 " and managers provide asynchronous feedback. SalesHood emphasizes peer-to-peer"
 " learning and community-driven enablement, where top performers share winning"
 " techniques with the team."
 ),
 "Demo Automation": (
 "Interactive demo platforms let enablement teams build self-service product experiences"
 " that prospects explore at their own pace. Storylane is the fastest to deploy, with"
 " a Chrome extension that captures your product and turns it into an interactive"
 " walkthrough in minutes. Navattic specializes in website-embedded demos for"
 " product-led growth. Consensus adds video narration to guided demo paths and provides"
 " analytics on how buying committee members interact with the demo."
 ),
 "Digital Sales Rooms": (
 "Digital sales rooms provide a shared workspace where reps and buyers collaborate"
 " throughout the deal. Dock combines mutual action plans, content sharing, and"
 " stakeholder tracking in a clean interface that enterprise buyers trust. Aligned"
 " focuses on buyer engagement analytics, showing you which stakeholders viewed which"
 " content and for how long. Trumpet offers a visually rich sales room experience with"
 " custom branding and interactive elements that stand out from standard file-sharing"
 " approaches."
 ),
 },
 "faqs": [
 {
 "question": "Do I need a dedicated content management platform, or will Google Drive work?",
 "answer": (
 "Google Drive works until it doesn't. Once you have 50+ sales assets across multiple"
 " products, personas, and deal stages, reps can't find what they need. A dedicated"
 " platform like Highspot or Showpad adds search, recommendations, CRM integration,"
 " and usage analytics that tell you which content closes deals. Invest"
 " when your reps regularly complain about finding the right materials."
 ),
 },
 {
 "question": "How do I measure enablement program effectiveness?",
 "answer": (
 "Track three tiers. Activity metrics: content usage rates, training completion,"
 " and certification scores. Behavior metrics: are reps using recommended content"
 " in deals, applying trained techniques on calls, and following prescribed processes?"
 " Outcome metrics: new hire ramp time, win rate changes, and average deal size"
 " improvements. The activity metrics are easy to measure. The outcome metrics"
 " prove the business impact."
 ),
 },
 {
 "question": "What's more important, content management or coaching?",
 "answer": (
 "Coaching produces faster, more measurable results. A rep who improves their"
 " discovery technique or objection handling sees immediate pipeline impact. Content"
 " management is a longer-term investment that compounds as your library grows and"
 " reps develop the habit of using it. If you can only pick one first, start with"
 " coaching. Layer content management in once your coaching program is established."
 ),
 },
 {
 "question": "Should enablement own demo automation tools?",
 "answer": (
 "Yes. Enablement should own the demo content and templates, even if AEs create"
 " their own customized versions for specific deals. Enablement ensures brand"
 " consistency, messaging accuracy, and that demos reflect the latest product"
 " capabilities. The demo library is a content asset, and content management is"
 " core enablement territory."
 ),
 },
 {
 "question": "How do I get executive buy-in for enablement tools?",
 "answer": (
 "Connect enablement metrics to revenue outcomes. Show the correlation between"
 " reps who complete training and their quota attainment. Demonstrate how content"
 " usage in deals correlates with win rates. Calculate the cost of extending new"
 " hire ramp time by even one week across your team. Frame enablement tools as"
 " revenue infrastructure, because that's what they are."
 ),
 },
 ],
}
