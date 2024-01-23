from django.contrib import admin
from .models import VirtualArtWorkForm, PerformingArtForm, LiteraryWorkForm, SoundRecordingForm, SerialWorkForm
from django.urls import reverse, path
from django.utils.safestring import mark_safe


class VirtualArtWorkFormAdmin(admin.ModelAdmin):
	def has_add_permission(self, request):
		return False

	list_display = [
		'id',
		'user',
		'form_name',
		'submitted_at',
		'new_form',
		'paid',
		'get_pdf'
	]
	# readonly_fields = [
	# 	'name',
	# 	'email_address',
	# 	'mailing_address',
	# 	'city',
	# 	'state',
	# 	'zipcode',
	# 	'title_of_work',
	# 	'prior_title',
	# 	'title_of_collective_work',
	# 	'volume',
	# 	'number',
	# 	'issue_date',
	# 	'pages',
	# 	'name_of_author',
	# 	'year_of_birth',
	# 	'year_of_death',
	# 	'work_for_hire',
	# 	'citizen_of',
	# 	'domiciled_of',
	# 	'authorship_anonymous',
	# 	'authorship_pseudonymous',
	# 	'nature_of_authorship',
	# 	'year_of_authorship',
	# 	'date_of_authorship',
	# 	'nation',
	# 	'claimant_name',
	# 	'reciepient_name',
	# 	'how_obtained_ownership',
	# 	'previously_registered',
	# 	'first_published_edition_of_work',
	# 	'first_application_by_the_author',
	# 	'changed_version_of_the_work',
	# 	'prior_reg_number',
	# 	'prior_reg_year',
	# 	'identify_preexisting_work',
	# 	'describe_preexisting_work',
	# 	'file',
	# 	'employer_name',
	# 	'employer_date_of_birth',
	# 	'date_of_hiring',
	# 	'employer_address',
	# 	'date_of_employing_copyright',
	# 	'sign_image',
	# 	'certification_name',
	# 	'continuation_title',
	# 	'name_and_address',
	# 	'name_of_author_1',
	# 	'year_of_birth_1',
	# 	'year_of_death_1',
	# 	'work_for_hire_1',
	# 	'citizen_of_1',
	# 	'domiciled_of_1',
	# 	'authorship_anonymous_1',
	# 	'authorship_pseudonymous_1',
	# 	'nature_of_authorship_1',
	# 	'name_of_author_2',
	# 	'year_of_birth_2',
	# 	'year_of_death_2',
	# 	'work_for_hire_2',
	# 	'citizen_of_2',
	# 	'domiciled_of_2',
	# 	'authorship_anonymous_2',
	# 	'authorship_pseudonymous_2',
	# 	'nature_of_authorship_2',
	# 	'name_of_author_3',
	# 	'year_of_birth_3',
	# 	'year_of_death_3',
	# 	'work_for_hire_3',
	# 	'citizen_of_3',
	# 	'domiciled_of_3',
	# 	'authorship_anonymous_3',
	# 	'authorship_pseudonymous_3',
	# 	'nature_of_authorship_3',
	# 	'continuation_name',
	# 	'continuation_date',
	# 	'continuation_address',
	# 	'continuation_city',
	# 	'continuation_state',
	# 	'continuation_zipcode',
	# ]

	def get_pdf(self, instance):
		if instance.id:
			pdf_url = reverse('pdf:vapdf', args={instance.id})
			return mark_safe(f"<a href='{pdf_url}' class='btn'>Get PDF</span>")
		else:
			return ""

	get_pdf.short_description = "Get PDF"

		# pdf = generate_pdf(template, dict)
		# return HttpResponse(pdf, content_type='application/pdf')
		# if pdf:
		# 	response = HttpResponse(pdf, content_type='application/pdf')
		# 	filename = "Invoice_%s.pdf" % ("12341231")
		# 	content = "inline; filename='%s'" % (filename)
		# 	download = request.GET.get("download")
		# 	if download:
		# 		content = "attachment; filename='%s'" % (filename)
		# 	response['Content-Disposition'] = content
		# 	return response
		# return HttpResponse("Not found")
	fieldsets = (
		(
			'New Form or Paying info',{
				'fields':(
					'new_form',
					'paid',
				)
			}
		),
		(
			'Start of form',{
			'fields': (
				'name',
				'email_address',
				'mailing_address',
				'city',
				'state',
				'zipcode'
				)
			}
		),
		(
			'SECTION 1', {
				'fields': (
					'title_of_work',
					'prior_title',
					'title_of_collective_work',
					'volume',
					'number',
					'issue_date',
					'pages',
				)
			}
		),
		(
			'SECTION 2', {
				'fields': (
					'name_of_author',
					'year_of_birth',
					'year_of_death',
					'work_for_hire',
					'citizen_of',
					'domiciled_of',
					'authorship_anonymous',
					'authorship_pseudonymous',
					# 'nature_of_authorship',
				)
			}
		),
		(
			'SECTION 3', {
				'fields': (
					'year_of_authorship',
					# 'date_of_authorship',
					'day',
					'month',
					'year',
					'nation',
				)
			}
		),
		(
			'SECTION 4', {
				'fields': (
					'claimant_name',
					'reciepient_name',
					'how_obtained_ownership',
				)
			}
		),
		(
			'SECTION 5', {
				'fields': (
					'previously_registered',
					'first_published_edition_of_work',
					'first_application_by_the_author',
					'changed_version_of_the_work',
					'prior_reg_number',
					'prior_reg_year',
				)
			}
		),
		(
			'SECTION 6', {
				'fields': (
					'identify_preexisting_work',
					'describe_preexisting_work'
				)
			}
		),
		(
			'Files Uploaded By The User', {
				'fields': (
					'file',
				)
			}
		),
		(
			'Power Of Attorney', {
				'fields': (
					'employer_name',
					'employer_date_of_birth',
					'date_of_hiring',
					'employer_address',
					'date_of_employing_copyright',
					'sign_image'
				)
			}
		),
		(
			'Last Secton Except Addeundum_Form', {
				'fields': (
					'certification_name',
				)
			}
		),
		(
			'_____________________________________________FROM HERE CONTINUATION SHEET START_____________________________________________', {
				'fields': (
				)
			}
		),
		(
			'CONTINUATION_TITLE', {
				'fields': (
					'continuation_title',
					'name_and_address',
				)
			}
		),
		(
			'CONTINUATION_AUTHOR_1', {
				'fields': (
					'name_of_author_1',
					'year_of_birth_1',
					'year_of_death_1',
					'work_for_hire_1',
					'citizen_of_1',
					'domiciled_of_1',
					'authorship_anonymous_1',
					'authorship_pseudonymous_1',
					'nature_of_authorship_1',
				)
			}
		),
		(
			'CONTINUATION_AUTHOR_2', {
				'fields': (
					'name_of_author_2',
					'year_of_birth_2',
					'year_of_death_2',
					'work_for_hire_2',
					'citizen_of_2',
					'domiciled_of_2',
					'authorship_anonymous_2',
					'authorship_pseudonymous_2',
					'nature_of_authorship_2',
				)
			}
		),
		(
			'CONTINUATION_AUTHOR_3', {
				'fields': (
					'name_of_author_3',
					'year_of_birth_3',
					'year_of_death_3',
					'work_for_hire_3',
					'citizen_of_3',
					'domiciled_of_3',
					'authorship_anonymous_3',
					'authorship_pseudonymous_3',
					'nature_of_authorship_3',

				)
			}
		),
		(
			'CONTINUATION FORM LAST FIELDS AFTER AUTHOR', {
				'fields': (
					'continuation_name',
					'continuation_date',
					'continuation_address',
					'continuation_city',
					'continuation_state',
					'continuation_zipcode',
				)
			}
		),
	)
admin.site.register(VirtualArtWorkForm, VirtualArtWorkFormAdmin)


class LiteraryWorkFormAdmin(admin.ModelAdmin):
	def has_add_permission(self, request):
		return False

	list_display = [
		'user',
		'form_name',
		'submitted_at',
		'new_form',
		'paid',
		'get_pdf'
	]

	def get_pdf(self, instance):
		if instance.id:
			pdf_url = reverse('pdf:txpdf', args={instance.id})
			return mark_safe(f"<a href='{pdf_url}' class='btn'>Get PDF</span>")
		else:
			return ""

	get_pdf.short_description = "Get PDF"

	# readonly_fields = [
	# 	'name',
	# 	'email_address',
	# 	'mailing_address',
	# 	'city',
	# 	'state',
	# 	'zipcode',
	# 	'title_of_work',
	# 	'prior_title',
	# 	'title_of_collective_work',
	# 	'volume',
	# 	'number',
	# 	'issue_date',
	# 	'pages',
	# 	'name_of_author',
	# 	'year_of_birth',
	# 	'year_of_death',
	# 	'work_for_hire',
	# 	'citizen_of',
	# 	'domiciled_of',
	# 	'authorship_anonymous',
	# 	'authorship_pseudonymous',
	# 	'nature_of_authorship',
	# 	'year_of_authorship',
	# 	'date_of_authorship',
	# 	'nation',
	# 	'claimant_name',
	# 	'reciepient_name',
	# 	'how_obtained_ownership',
	# 	'previously_registered',
	# 	'first_published_edition_of_work',
	# 	'first_application_by_the_author',
	# 	'changed_version_of_the_work',
	# 	'prior_reg_number',
	# 	'prior_reg_year',
	# 	'identify_preexisting_work',
	# 	'describe_preexisting_work',
	# 	'file',
	# 	'employer_name',
	# 	'employer_date_of_birth',
	# 	'date_of_hiring',
	# 	'employer_address',
	# 	'date_of_employing_copyright',
	# 	'sign_image',
	# 	'certification_name',
	# 	'continuation_title',
	# 	'name_and_address',
	# 	'name_of_author_1',
	# 	'year_of_birth_1',
	# 	'year_of_death_1',
	# 	'work_for_hire_1',
	# 	'citizen_of_1',
	# 	'domiciled_of_1',
	# 	'authorship_anonymous_1',
	# 	'authorship_pseudonymous_1',
	# 	'nature_of_authorship_1',
	# 	'name_of_author_2',
	# 	'year_of_birth_2',
	# 	'year_of_death_2',
	# 	'work_for_hire_2',
	# 	'citizen_of_2',
	# 	'domiciled_of_2',
	# 	'authorship_anonymous_2',
	# 	'authorship_pseudonymous_2',
	# 	'nature_of_authorship_2',
	# 	'name_of_author_3',
	# 	'year_of_birth_3',
	# 	'year_of_death_3',
	# 	'work_for_hire_3',
	# 	'citizen_of_3',
	# 	'domiciled_of_3',
	# 	'authorship_anonymous_3',
	# 	'authorship_pseudonymous_3',
	# 	'nature_of_authorship_3',
	# 	'continuation_name',
	# 	'continuation_date',
	# 	'continuation_address',
	# 	'continuation_city',
	# 	'continuation_state',
	# 	'continuation_zipcode',
	# ]

	fieldsets = (
		(
			'New Form or Paying info',{
				'fields':(
					'new_form',
					'paid',
				)
			}
		),
		(
			'Start of form',{
			'fields': (
				'name',
				'email_address',
				'mailing_address',
				'city',
				'state',
				'zipcode'
				)
			}
		),
		(
			'SECTION 1', {
				'fields': (
					'title_of_work',
					'prior_title',
					'title_of_collective_work',
					'volume',
					'number',
					'issue_date',
					'pages',
				)
			}
		),
		(
			'SECTION 2', {
				'fields': (
					'name_of_author',
					'year_of_birth',
					'year_of_death',
					'work_for_hire',
					'citizen_of',
					'domiciled_of',
					'authorship_anonymous',
					'authorship_pseudonymous',
					'nature_of_authorship',
				)
			}
		),
		(
			'SECTION 3', {
				'fields': (
					'year_of_authorship',
					'day',
					'month',
					'year',
					'nation',
				)
			}
		),
		(
			'SECTION 4', {
				'fields': (
					'claimant_name',
					'reciepient_name',
					'how_obtained_ownership',
				)
			}
		),
		(
			'SECTION 5', {
				'fields': (
					'previously_registered',
					'first_published_edition_of_work',
					'first_application_by_the_author',
					'changed_version_of_the_work',
					'prior_reg_number',
					'prior_reg_year',
				)
			}
		),
		(
			'SECTION 6', {
				'fields': (
					'identify_preexisting_work',
					'describe_preexisting_work'
				)
			}
		),
		(
			'Files Uploaded By The User', {
				'fields': (
					'file',
				)
			}
		),
		(
			'Power Of Attorney', {
				'fields': (
					'employer_name',
					'employer_date_of_birth',
					'date_of_hiring',
					'employer_address',
					'date_of_employing_copyright',
					'sign_image'
				)
			}
		),
		(
			'Last Secton Except Addeundum_Form', {
				'fields': (
					'certification_name',
				)
			}
		),
		(
			'_____________________________________________FROM HERE CONTINUATION SHEET START_____________________________________________', {
				'fields': (
				)
			}
		),
		(
			'CONTINUATION_TITLE', {
				'fields': (
					'continuation_title',
					'name_and_address',
				)
			}
		),
		(
			'CONTINUATION_AUTHOR_1', {
				'fields': (
					'name_of_author_1',
					'year_of_birth_1',
					'year_of_death_1',
					'work_for_hire_1',
					'citizen_of_1',
					'domiciled_of_1',
					'authorship_anonymous_1',
					'authorship_pseudonymous_1',
					'nature_of_authorship_1',
				)
			}
		),
		(
			'CONTINUATION_AUTHOR_2', {
				'fields': (
					'name_of_author_2',
					'year_of_birth_2',
					'year_of_death_2',
					'work_for_hire_2',
					'citizen_of_2',
					'domiciled_of_2',
					'authorship_anonymous_2',
					'authorship_pseudonymous_2',
					'nature_of_authorship_2',
				)
			}
		),
		(
			'CONTINUATION_AUTHOR_3', {
				'fields': (
					'name_of_author_3',
					'year_of_birth_3',
					'year_of_death_3',
					'work_for_hire_3',
					'citizen_of_3',
					'domiciled_of_3',
					'authorship_anonymous_3',
					'authorship_pseudonymous_3',
					'nature_of_authorship_3',

				)
			}
		),
		(
			'CONTINUATION FORM LAST FIELDS AFTER AUTHOR', {
				'fields': (
					'continuation_name',
					'continuation_date',
					'continuation_address',
					'continuation_city',
					'continuation_state',
					'continuation_zipcode',
				)
			}
		),
	)
admin.site.register(LiteraryWorkForm, LiteraryWorkFormAdmin)


class SoundRecordingFormAdmin(admin.ModelAdmin):
	def has_add_permission(self, request):
		return False
	list_display = [
		'id',
		'user',
		'form_name',
		'submitted_at',
		'new_form',
		'paid',
		'get_pdf'
	]

	def get_pdf(self, instance):
		if instance.id:
			pdf_url = reverse('pdf:srpdf', args={instance.id})
			return mark_safe(f"<a href='{pdf_url}' class='btn'>Get PDF</span>")
		else:
			return ""

	get_pdf.short_description = "Get PDF"
	readonly_fields = [
		# 'name',
		# 'email_address',
		#
		# 'title_of_work',
		# 'prior_title',
		#
		# 'name_of_author',
		# 'year_of_birth',
		# 'year_of_death',
		# 'work_for_hire',
		# 'citizen_of',
		# 'domiciled_of',
		# 'authorship_anonymous',
		# 'authorship_pseudonymous',
		# 'nature_of_authorship',
		# 'year_of_authorship',
		# 'date_of_authorship',
		# 'nation',
		# 'claimant_name',
		# 'reciepient_name',
		# 'how_obtained_ownership',
		# 'previously_registered',
		# 'first_published_edition_of_work',
		# 'first_application_by_the_author',
		# 'changed_version_of_the_work',
		# 'prior_reg_number',
		# 'prior_reg_year',
		# 'identify_preexisting_work',
		# 'describe_preexisting_work',
		# 'file',
		# 'employer_name',
		# 'employer_date_of_birth',
		# 'date_of_hiring',
		# 'employer_address',
		# 'date_of_employing_copyright',
		# 'sign_image',
		# 'certification_name',
		# 'continuation_title',
		# 'name_and_address',
		# 'name_of_author_1',
		# 'year_of_birth_1',
		# 'year_of_death_1',
		# 'work_for_hire_1',
		# 'citizen_of_1',
		# 'domiciled_of_1',
		# 'authorship_anonymous_1',
		# 'authorship_pseudonymous_1',
		# 'nature_of_authorship_1',
		# 'name_of_author_2',
		# 'year_of_birth_2',
		# 'year_of_death_2',
		# 'work_for_hire_2',
		# 'citizen_of_2',
		# 'domiciled_of_2',
		# 'authorship_anonymous_2',
		# 'authorship_pseudonymous_2',
		# 'nature_of_authorship_2',
		# 'name_of_author_3',
		# 'year_of_birth_3',
		# 'year_of_death_3',
		# 'work_for_hire_3',
		# 'citizen_of_3',
		# 'domiciled_of_3',
		# 'authorship_anonymous_3',
		# 'authorship_pseudonymous_3',
		# 'nature_of_authorship_3',
		# 'continuation_name',
		# 'continuation_date',
		# 'continuation_address',
		# 'continuation_city',
		# 'continuation_state',
		# 'continuation_zipcode',
	]


	fieldsets = (
		(
			'New Form or Paying info',{
				'fields':(
					'new_form',
					'paid',
				)
			}
		),
		(
			'Start of form',{
			'fields': (
				'name',
				'email_address',
				)
			}
		),
		(
			'SECTION 1', {
				'fields': (
					'title_of_work',
					'prior_title',
				)
			}
		),
		(
			'SECTION 2', {
				'fields': (
					'name_of_author',
					'year_of_birth',
					'year_of_death',
					'work_for_hire',
					'citizen_of',
					'domiciled_of',
					'authorship_anonymous',
					'authorship_pseudonymous',
					'nature_of_authorship',
				)
			}
		),
		(
			'SECTION 3', {
				'fields': (
					'year_of_authorship',
					'day',
					'month',
					'year',
					'nation',
				)
			}
		),
		(
			'SECTION 4', {
				'fields': (
					'claimant_name',
					'reciepient_name',
					'how_obtained_ownership',
					'claimant_address',
				)
			}
		),
		(
			'SECTION 5', {
				'fields': (
					'previously_registered',
					'first_published_edition_of_work',
					'first_application_by_the_author',
					'changed_version_of_the_work',
					'prior_reg_number',
					'prior_reg_year',
				)
			}
		),
		(
			'SECTION 6', {
				'fields': (
					'identify_preexisting_work',
					'describe_preexisting_work'
				)
			}
		),
		(
			'Files Uploaded By The User', {
				'fields': (
					'file',
				)
			}
		),
		(
			'Power Of Attorney', {
				'fields': (
					'employer_name',
					'employer_date_of_birth',
					'date_of_hiring',
					'employer_address',
					'date_of_employing_copyright',
					'city',
					'state',
					'zipcode',
					'sign_image'
				)
			}
		),
		(
			'Last Secton Except Addeundum_Form', {
				'fields': (
					'certification_name',
				)
			}
		),
		(
			'_____________________________________________FROM HERE CONTINUATION SHEET START_____________________________________________', {
				'fields': (
				)
			}
		),
		(
			'CONTINUATION_TITLE', {
				'fields': (
					'continuation_title',
					'name_and_address',
				)
			}
		),
		(
			'CONTINUATION_AUTHOR_1', {
				'fields': (
					'name_of_author_1',
					'year_of_birth_1',
					'year_of_death_1',
					'work_for_hire_1',
					'citizen_of_1',
					'domiciled_of_1',
					'authorship_anonymous_1',
					'authorship_pseudonymous_1',
					'nature_of_authorship_1',
				)
			}
		),
		(
			'CONTINUATION_AUTHOR_2', {
				'fields': (
					'name_of_author_2',
					'year_of_birth_2',
					'year_of_death_2',
					'work_for_hire_2',
					'citizen_of_2',
					'domiciled_of_2',
					'authorship_anonymous_2',
					'authorship_pseudonymous_2',
					'nature_of_authorship_2',
				)
			}
		),
		(
			'CONTINUATION_AUTHOR_3', {
				'fields': (
					'name_of_author_3',
					'year_of_birth_3',
					'year_of_death_3',
					'work_for_hire_3',
					'citizen_of_3',
					'domiciled_of_3',
					'authorship_anonymous_3',
					'authorship_pseudonymous_3',
					'nature_of_authorship_3',

				)
			}
		),
		(
			'CONTINUATION FORM LAST FIELDS AFTER AUTHOR', {
				'fields': (
					'continuation_name',
					'continuation_date',
					'continuation_address',
					'continuation_city',
					'continuation_state',
					'continuation_zipcode',
				)
			}
		),
	)
admin.site.register(SoundRecordingForm, SoundRecordingFormAdmin)


class SerialWorkFormAdmin(admin.ModelAdmin):
	def has_add_permission(self, request):
		return False



	list_display = [
		'user',
		'form_name',
		'submitted_at',
		'new_form',
		'paid',
		'get_pdf'
	]
	def get_pdf(self, instance):
		if instance.id:
			pdf_url = reverse('pdf:sepdf', args={instance.id})
			return mark_safe(f"<a href='{pdf_url}' class='btn'>Get PDF</span>")
		else:
			return ""

	get_pdf.short_description = "Get PDF"
	readonly_fields = [
		# 'name',
		# 'email_address',
		#
		# 'title_of_work',
		# 'volume',
		# 'number',
		# 'date_on_copies',
		# 'frequency',
		# 'prior_title',
		#
		# 'name_of_author',
		# 'year_of_birth',
		# 'year_of_death',
		# 'work_for_hire',
		# 'citizen_of',
		# 'domiciled_of',
		# 'authorship_anonymous',
		# 'authorship_pseudonymous',
		# 'nature_of_authorship',
		# 'year_of_authorship',
		# 'date_of_authorship',
		# 'nation',
		# 'claimant_name',
		# 'reciepient_name',
		# 'how_obtained_ownership',
		# 'previously_registered',
		# 'first_published_edition_of_work',
		# 'first_application_by_the_author',
		# 'changed_version_of_the_work',
		# 'prior_reg_number',
		# 'prior_reg_year',
		# 'identify_preexisting_work',
		# 'describe_preexisting_work',
		# 'file',
		# 'employer_name',
		# 'employer_date_of_birth',
		# 'date_of_hiring',
		# 'employer_address',
		# 'date_of_employing_copyright',
		# 'sign_image',
		# 'certification_name',
		# 'continuation_title',
		# 'name_and_address',
		# 'name_of_author_1',
		# 'year_of_birth_1',
		# 'year_of_death_1',
		# 'work_for_hire_1',
		# 'citizen_of_1',
		# 'domiciled_of_1',
		# 'authorship_anonymous_1',
		# 'authorship_pseudonymous_1',
		# 'nature_of_authorship_1',
		# 'name_of_author_2',
		# 'year_of_birth_2',
		# 'year_of_death_2',
		# 'work_for_hire_2',
		# 'citizen_of_2',
		# 'domiciled_of_2',
		# 'authorship_anonymous_2',
		# 'authorship_pseudonymous_2',
		# 'nature_of_authorship_2',
		# 'name_of_author_3',
		# 'year_of_birth_3',
		# 'year_of_death_3',
		# 'work_for_hire_3',
		# 'citizen_of_3',
		# 'domiciled_of_3',
		# 'authorship_anonymous_3',
		# 'authorship_pseudonymous_3',
		# 'nature_of_authorship_3',
		# 'continuation_name',
		# 'continuation_date',
		# 'continuation_address',
		# 'continuation_city',
		# 'continuation_state',
		# 'continuation_zipcode',
	]

	fieldsets = (
		(
			'New Form or Paying info',{
				'fields':(
					'new_form',
					'paid',
				)
			}
		),
		(
			'Start of form',{
			'fields': (
				'name',
				'email_address',
				)
			}
		),
		(
			'SECTION 1', {
				'fields': (
					'title_of_work',
					'volume',
					'number',
					'date_on_copies',
					'frequency',
					'prior_title',
				)
			}
		),
		(
			'SECTION 2', {
				'fields': (
					'name_of_author',
					'year_of_birth',
					'year_of_death',
					'work_for_hire',
					'citizen_of',
					'domiciled_of',
					'authorship_anonymous',
					'authorship_pseudonymous',
					'nature_of_authorship',
				)
			}
		),
		(
			'SECTION 3', {
				'fields': (
					'year_of_authorship',
					'month',
					'day',
					'year',
					'nation',
				)
			}
		),
		(
			'SECTION 4', {
				'fields': (
					'claimant_name',
					'reciepient_name',
					'how_obtained_ownership',
					'claimant_address'
				)
			}
		),
		(
			'SECTION 5', {
				'fields': (
					'previously_registered',
					'first_published_edition_of_work',
					'first_application_by_the_author',
					'changed_version_of_the_work',
					'prior_reg_number',
					'prior_reg_year',
				)
			}
		),
		(
			'SECTION 6', {
				'fields': (
					'identify_preexisting_work',
					'describe_preexisting_work'
				)
			}
		),
		(
			'Files Uploaded By The User', {
				'fields': (
					'file',
				)
			}
		),
		(
			'Power Of Attorney', {
				'fields': (
					'employer_name',
					'employer_date_of_birth',
					'date_of_hiring',
					'employer_address',
					'date_of_employing_copyright',
					'city',
					'state',
					'zipcode',
					'sign_image'
				)
			}
		),
		(
			'Last Secton Except Addeundum_Form', {
				'fields': (
					'certification_name',
				)
			}
		),
		(
			'_____________________________________________FROM HERE CONTINUATION SHEET START_____________________________________________', {
				'fields': (
				)
			}
		),
		(
			'CONTINUATION_TITLE', {
				'fields': (
					'continuation_title',
					'name_and_address',
				)
			}
		),
		(
			'CONTINUATION_AUTHOR_1', {
				'fields': (
					'name_of_author_1',
					'year_of_birth_1',
					'year_of_death_1',
					'work_for_hire_1',
					'citizen_of_1',
					'domiciled_of_1',
					'authorship_anonymous_1',
					'authorship_pseudonymous_1',
					'nature_of_authorship_1',
				)
			}
		),
		(
			'CONTINUATION_AUTHOR_2', {
				'fields': (
					'name_of_author_2',
					'year_of_birth_2',
					'year_of_death_2',
					'work_for_hire_2',
					'citizen_of_2',
					'domiciled_of_2',
					'authorship_anonymous_2',
					'authorship_pseudonymous_2',
					'nature_of_authorship_2',
				)
			}
		),
		(
			'CONTINUATION_AUTHOR_3', {
				'fields': (
					'name_of_author_3',
					'year_of_birth_3',
					'year_of_death_3',
					'work_for_hire_3',
					'citizen_of_3',
					'domiciled_of_3',
					'authorship_anonymous_3',
					'authorship_pseudonymous_3',
					'nature_of_authorship_3',

				)
			}
		),
		(
			'CONTINUATION FORM LAST FIELDS AFTER AUTHOR', {
				'fields': (
					'continuation_name',
					'continuation_date',
					'continuation_address',
					'continuation_city',
					'continuation_state',
					'continuation_zipcode',
				)
			}
		),
	)
admin.site.register(SerialWorkForm, SerialWorkFormAdmin)


class PerformingArtFormAdmin(admin.ModelAdmin):
	def has_add_permission(self, request):
		return False

	list_display = [
		'user',
		'form_name',
		'submitted_at',
		'new_form',
		'paid',
		'get_pdf'
	]

	def get_pdf(self, instance):
		if instance.id:
			pdf_url = reverse('pdf:papdf', args={instance.id})
			return mark_safe(f"<a href='{pdf_url}' class='btn'>Get PDF</span>")
		else:
			return ""

	get_pdf.short_description = "Get PDF"

	# readonly_fields = [
	# 	'name',
	# 	'email_address',
	# 	'title_of_work',
	# 	'prior_title',
	# 	'nature_of_work',
	# 	'name_of_author',
	# 	'year_of_birth',
	# 	'year_of_death',
	# 	'work_for_hire',
	# 	'citizen_of',
	# 	'domiciled_of',
	# 	'authorship_anonymous',
	# 	'authorship_pseudonymous',
	# 	'nature_of_authorship',
	# 	'year_of_authorship',
	# 	'date_of_authorship',
	# 	'nation',
	# 	'claimant_name',
	# 	'reciepient_name',
	# 	'how_obtained_ownership',
	# 	'previously_registered',
	# 	'first_published_edition_of_work',
	# 	'first_application_by_the_author',
	# 	'changed_version_of_the_work',
	# 	'prior_reg_number',
	# 	'prior_reg_year',
	# 	'identify_preexisting_work',
	# 	'describe_preexisting_work',
	# 	'file',
	# 	'employer_name',
	# 	'employer_date_of_birth',
	# 	'date_of_hiring',
	# 	'employer_address',
	# 	'date_of_employing_copyright',
	# 	'sign_image',
	# 	'certification_name',
	# 	'continuation_title',
	# 	'name_and_address',
	# 	'name_of_author_1',
	# 	'year_of_birth_1',
	# 	'year_of_death_1',
	# 	'work_for_hire_1',
	# 	'citizen_of_1',
	# 	'domiciled_of_1',
	# 	'authorship_anonymous_1',
	# 	'authorship_pseudonymous_1',
	# 	'nature_of_authorship_1',
	# 	'name_of_author_2',
	# 	'year_of_birth_2',
	# 	'year_of_death_2',
	# 	'work_for_hire_2',
	# 	'citizen_of_2',
	# 	'domiciled_of_2',
	# 	'authorship_anonymous_2',
	# 	'authorship_pseudonymous_2',
	# 	'nature_of_authorship_2',
	# 	'name_of_author_3',
	# 	'year_of_birth_3',
	# 	'year_of_death_3',
	# 	'work_for_hire_3',
	# 	'citizen_of_3',
	# 	'domiciled_of_3',
	# 	'authorship_anonymous_3',
	# 	'authorship_pseudonymous_3',
	# 	'nature_of_authorship_3',
	# 	'continuation_name',
	# 	'continuation_date',
	# 	'continuation_address',
	# 	'continuation_city',
	# 	'continuation_state',
	# 	'continuation_zipcode',
	# ]

	fieldsets = (
		(
			'New Form or Paying info',{
				'fields':(
					'new_form',
					'paid',
				)
			}
		),
		(
			'Start of form',{
			'fields': (
				'name',
				'email_address',
				)
			}
		),
		(
			'SECTION 1', {
				'fields': (
					'title_of_work',
					'prior_title',
					'nature_of_work',
				)
			}
		),
		(
			'SECTION 2', {
				'fields': (
					'name_of_author',
					'year_of_birth',
					'year_of_death',
					'work_for_hire',
					'citizen_of',
					'domiciled_of',
					'authorship_anonymous',
					'authorship_pseudonymous',
					'nature_of_authorship',
				)
			}
		),
		(
			'SECTION 3', {
				'fields': (
					'year_of_authorship',
					'month',
					'day',
					'year',
					'nation',
				)
			}
		),
		(
			'SECTION 4', {
				'fields': (
					'claimant_name',
					'reciepient_name',
					'how_obtained_ownership',
				)
			}
		),
		(
			'SECTION 5', {
				'fields': (
					'previously_registered',
					'first_published_edition_of_work',
					'first_application_by_the_author',
					'changed_version_of_the_work',
					'prior_reg_number',
					'prior_reg_year',
				)
			}
		),
		(
			'SECTION 6', {
				'fields': (
					'identify_preexisting_work',
					'describe_preexisting_work'
				)
			}
		),
		(
			'Files Uploaded By The User', {
				'fields': (
					'file',
				)
			}
		),
		(
			'Power Of Attorney', {
				'fields': (
					'employer_name',
					'employer_date_of_birth',
					'date_of_hiring',
					'employer_address',
					'date_of_employing_copyright',
					'city',
					'state',
					'zipcode',
					'sign_image'
				)
			}
		),
		(
			'Last Secton Except Addeundum_Form', {
				'fields': (
					'certification_name',
				)
			}
		),
		(
			'_____________________________________________FROM HERE CONTINUATION SHEET START_____________________________________________', {
				'fields': (
				)
			}
		),
		(
			'CONTINUATION_TITLE', {
				'fields': (
					'continuation_title',
					'name_and_address',
				)
			}
		),
		(
			'CONTINUATION_AUTHOR_1', {
				'fields': (
					'name_of_author_1',
					'year_of_birth_1',
					'year_of_death_1',
					'work_for_hire_1',
					'citizen_of_1',
					'domiciled_of_1',
					'authorship_anonymous_1',
					'authorship_pseudonymous_1',
					'nature_of_authorship_1',
				)
			}
		),
		(
			'CONTINUATION_AUTHOR_2', {
				'fields': (
					'name_of_author_2',
					'year_of_birth_2',
					'year_of_death_2',
					'work_for_hire_2',
					'citizen_of_2',
					'domiciled_of_2',
					'authorship_anonymous_2',
					'authorship_pseudonymous_2',
					'nature_of_authorship_2',
				)
			}
		),
		(
			'CONTINUATION_AUTHOR_3', {
				'fields': (
					'name_of_author_3',
					'year_of_birth_3',
					'year_of_death_3',
					'work_for_hire_3',
					'citizen_of_3',
					'domiciled_of_3',
					'authorship_anonymous_3',
					'authorship_pseudonymous_3',
					'nature_of_authorship_3',

				)
			}
		),
		(
			'CONTINUATION FORM LAST FIELDS AFTER AUTHOR', {
				'fields': (
					'continuation_name',
					'continuation_date',
					'continuation_address',
					'continuation_city',
					'continuation_state',
					'continuation_zipcode',
				)
			}
		),
	)
admin.site.register(PerformingArtForm, PerformingArtFormAdmin)