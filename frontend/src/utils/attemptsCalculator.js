/**
 * Calculates a rough estimate of remaining exam attempts based on date of
 * birth and each exam's structured age/session rules.
 *
 * This is a General-category, best-effort estimate for planning purposes -
 * NOT an official eligibility determination. Reserved categories typically
 * get age relaxation (noted per-exam where known), and exact cutoff dates
 * (e.g. "as on 1st August of the exam year") vary by year and notification,
 * which this calculator approximates using the person's exact age today.
 */

function getAgeInYears(dob, asOf = new Date()) {
  const diffMs = asOf - dob
  return diffMs / (1000 * 60 * 60 * 24 * 365.25)
}

export function calculateExamAttempts(dob, exam) {
  const age = getAgeInYears(dob)
  const { min_age, max_age, sessions_per_year, max_total_attempts } = exam

  // Not yet eligible (too young)
  if (min_age != null && age < min_age) {
    const yearsUntilEligible = min_age - age
    return {
      status: 'not-yet-eligible',
      age: age,
      message: `You'll become eligible in about ${formatYears(yearsUntilEligible)}.`,
      attemptsRemaining: null,
    }
  }

  // Aged out (too old)
  if (max_age != null && age >= max_age) {
    return {
      status: 'aged-out',
      age: age,
      message: `You're past the general-category upper age limit (${max_age} years) for this exam.`,
      attemptsRemaining: 0,
    }
  }

  // Currently eligible - estimate remaining attempts
  let attemptsRemaining = null
  let message = ''

  if (max_age == null) {
    // No upper age limit at all
    if (max_total_attempts != null) {
      attemptsRemaining = max_total_attempts
      message = `No upper age limit for this exam - you have up to ${max_total_attempts} total attempt(s) regardless of age.`
    } else {
      message = 'No upper age limit and no attempt cap for this exam - you can attempt it as many times as offered.'
    }
  } else {
    const yearsRemaining = max_age - age
    const sessionsPerYear = sessions_per_year || 1
    const estimatedByAge = Math.max(0, Math.floor(yearsRemaining * sessionsPerYear))

    attemptsRemaining = max_total_attempts != null
      ? Math.min(estimatedByAge, max_total_attempts)
      : estimatedByAge

    message = `Estimated ${attemptsRemaining} attempt(s) remaining before you age out at ${max_age} years` +
      (max_total_attempts != null ? ` (also capped at ${max_total_attempts} total attempts).` : '.')
  }

  return {
    status: 'eligible',
    age: age,
    message,
    attemptsRemaining,
  }
}

function formatYears(years) {
  if (years < 1) {
    const months = Math.round(years * 12)
    return `${months} month${months === 1 ? '' : 's'}`
  }
  return `${years.toFixed(1)} years`
}

export function formatAge(years) {
  const wholeYears = Math.floor(years)
  const months = Math.round((years - wholeYears) * 12)
  return months > 0 ? `${wholeYears} yrs ${months} mo` : `${wholeYears} yrs`
}
