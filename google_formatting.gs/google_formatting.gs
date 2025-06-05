function formatSheetAndTrimAssignees() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const templateSheet = ss.getSheetByName("Template");
  const targetSheet = ss.getSheetByName("Sync 0603-0654"); // Change this to match your current sheet being formatted

  if (!templateSheet || !targetSheet) {
    Logger.log("❌ Could not find 'Template' or target sheet.");
    return;
  }

  if (templateSheet.getName() === targetSheet.getName()) {
    Logger.log("❌ Template and target sheet are the same.");
    return;
  }

  // 🎨 Step 1: Copy conditional formatting rules from Template
  const templateRules = templateSheet.getConditionalFormatRules();
  const adjustedRules = templateRules.map(rule => {
    const newRanges = rule.getRanges().map(range =>
      targetSheet.getRange(range.getRow(), range.getColumn(), range.getNumRows(), range.getNumColumns())
    );
    return rule.copy().setRanges(newRanges).build();
  });

  // ➕ Step 2: Add new formatting for status-based colors (A–D)
  const lastRow = targetSheet.getLastRow();
  if (lastRow > 1) {
    const statusRange = targetSheet.getRange(`A2:D${lastRow}`);

    const blockedRule = SpreadsheetApp.newConditionalFormatRule()
      .whenFormulaSatisfied(`=$D2="Blocked"`)
      .setBackground("#f4cccc")  // Light orange
      .setRanges([statusRange])
      .build();

    const inProgressRule = SpreadsheetApp.newConditionalFormatRule()
      .whenFormulaSatisfied(`=$D2="In Progress"`)
      .setBackground("#fff2cc")  // Light yellow
      .setRanges([statusRange])
      .build();

    adjustedRules.push(blockedRule, inProgressRule);
  }

  targetSheet.setConditionalFormatRules(adjustedRules);
  Logger.log(`✅ All formatting rules applied to: ${targetSheet.getName()}`);

  // ✂️ Step 3: Trim assignee names to first name only (column C)
  const range = targetSheet.getDataRange();
  const values = range.getValues();

  for (let i = 1; i < values.length; i++) {
    const fullName = values[i][2]; // Column C
    if (typeof fullName === "string" && fullName.includes(" ")) {
      values[i][2] = fullName.split(" ")[0];
    }
  }

  range.setValues(values);
  Logger.log("🧹 Assignee names updated to first names only.");

  // 📐 Step 4: Center align columns B–F
  const centerRange = targetSheet.getRange(2, 2, lastRow - 1, 5); // B2:F
  centerRange.setHorizontalAlignment("center");
  Logger.log("📐 Columns B–F centered.");
}
