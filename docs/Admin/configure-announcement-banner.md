---
title: "Configuring announcement banners"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/configure-announcement-banner.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Configuring features and integrations"]
---

# Configuring announcement banners

Announcement banners display important messages to all users, such as system notices, or scheduled maintenance.

## How announcement banners work

Announcement banners display short messages at the top of the client interface to share tenant-wide information, warnings, or issues.

The banner is shown when a user logs in. If a user dismisses a banner, it reappears only if it is updated or at the next login.

Only one banner can exist at a time. When you update the banner, the new information replaces the previous content.

## When to use banners

Banners can be used, for example, to communicate issues, promote events, or encourage adoption of new features.

## Configuring a banner

Tenant administrators can configure announcement banners.

Do the following:

1. In the Administration activity center, go to Settings > Announcements.
2. Select a styling for the banner: Info, Warning, Error, or Resolved.
3. Enter the banner text (maximum 255 characters). Emojis are supported, but images are not.

   - The preview below the settings updates live, so you can check readability and appearance as you type.
4. (Optional) Add a link to the banner:

   1. Turn on the Link toggle.
   2. Enter the link text.
   3. Enter the link URL.
5. Set the start and end dates. Dates are stored in UTC, not your local time zone.

   Tip noteUse start and end dates to schedule banners, and update them as needed for recurring or repeated announcements.
6. Turn on the Apply toggle to activate the banner. The banner will appear to all users during the configured period.

Announcement banner settings with preview.

![Announcement banner settings.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_announcement_banner.png "Click to view full size")

### Example: Warning banner for scheduled maintenance

Use this type of banner to alert users about planned downtime or service issues, and include a link so users can access full details about the maintenance.

- Styling: Warning
- Text: "Planned maintenance on October 30. Service might be unavailable for up to 2 hours."
- Link text: "More information"
- Link URL: Link to a page with full details
- Start date: 2025-10-27
- End date: 2025-10-30

## Editing a banner

When you edit a field, your changes are saved automatically.

- For active banners, updates appear immediately for all users.
- For inactive banners, changes are saved only when all required fields are complete.
