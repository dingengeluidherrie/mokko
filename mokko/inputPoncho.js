/* @flow @jsx h */
import { h } from 'preact';
import classNames from 'classnames';

import './styles/input.less';

type Props = {
	/** A unique reference to the input element */
	reference: string,
	/** The name of the element */
	name: string,
	/** The type of input field */
	type: string,
	/** The placeholder to render inside the input element */
	placeholder: ?string,
	/** Whether the element is required or not */
	required?: boolean,
	/** Whether the element is disabled or not */
	disabled?: boolean,
	/** Whether the element is read only or not */
	readonly?: boolean,
	/** A pattern to use for validating the input */
	pattern?: string,
	/** Whether the element is loading */
	loading?: boolean,
	/** An optional additional class */
	class?: string,
	/** Whether the value is valid */
	valid?: boolean,
	/** Optional function to get the ref higher in the tree */
	inputRef?: Function,
};

/**
 * The input component can be used to render an ANWB styled input
 */
const Input = ({
	reference,
	name,
	type,
	placeholder,
	required,
	disabled,
	readonly,
	pattern,
	valid,
	loading,
	inputRef,
	class: className,
	...props
}: Props) => {
	const inputClassNames = classNames(
		'PONCHO-input',
		{
			'PONCHO-input--loading': loading,
			'PONCHO-input--valid': valid === true,
			'PONCHO-input--invalid': valid === false,
			'PONCHO-input--readonly': disabled || readonly,
		},
		className
	);

	return (
		<input
			class={inputClassNames}
			type={type}
			id={reference}
			name={name}
			placeholder={placeholder}
			required={required}
			disabled={disabled}
			pattern={pattern}
			aria-required={required}
			aria-disabled={disabled}
			aria-invalid={valid === false ? true : undefined}
			data-hj-suppress
			ref={inputRef}
			{...props}
		/>
	);
};

Input.defaultProps = {
	required: false,
	disabled: false,
};

export default Input;
