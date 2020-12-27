export class GradeSchool {
  constructor() {
    this._roster = {};
  }

  roster() {
    return JSON.parse(JSON.stringify(this._roster));
  }

  add(student, grade) {
    removeFromRoster(this._roster, student);
    addToRoster(this._roster, student, grade);
  }

  grade(number) {
    return [...(this._roster[number] || [])];
  }
}

const removeFromRoster = (roster, student) => {
  for (const grade of Object.values(roster)) {
    const index = grade.indexOf(student);
    if (index !== -1) grade.splice(index, 1);
  }
};

const addToRoster = (roster, student, grade) => {
  const students = roster[grade];
  roster[grade] = [...(students || []), student].sort();
};
